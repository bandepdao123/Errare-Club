"""Read-only source routing and paginated metadata lookup for local ER skills.

No network, generation, publishing, database creation or implicit full-text output.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inside(root, relative):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError("Path outside workspace")
    return path


def registry(root):
    return json.loads(inside(root, "00-Standards/skills.json").read_text(encoding="utf-8"))


def route(root, skill, task=None, mode=None, hashes=False):
    data = registry(root)
    if skill not in data["skills"]:
        raise ValueError("Unknown ER skill")
    entry = data["skills"][skill]
    task = task or entry["default_task"]
    if task not in entry["tasks"]:
        raise ValueError("Task is not supported by this skill")
    plan = entry["tasks"][task]
    if mode is not None and mode not in data["mode_sources"]:
        raise ValueError("Unknown source mode")
    paths = data["common_sources"] + plan["sources"]
    if plan.get("include_mode_sources"):
        if mode is None:
            raise ValueError("Choose product, reference or hybrid from the actual request")
        paths += data["mode_sources"][mode]
    sources = []
    for relative in dict.fromkeys(paths):
        path = inside(root, relative)
        if not path.is_file():
            raise ValueError("Missing required source: " + relative)
        item = {"path": relative}
        if hashes:
            item["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        sources.append(item)
    kinds = list(plan["data_kinds"])
    if plan.get("include_mode_sources") and mode == "product":
        kinds = [kind for kind in kinds if kind != "reference"]
    return {
        "skill": skill, "task": task, "mode": mode,
        "sources_to_open": sources, "lookup_kinds": kinds,
        "note": "Paths only, not a read receipt. Open required originals and actual task dependencies; no tool action is authorized by this plan.",
    }


def records(document):
    if not isinstance(document, dict):
        raise ValueError("Expected a JSON object record or items envelope")
    if "items" in document:
        if not isinstance(document["items"], list):
            raise ValueError("items must be an array")
        for index, item in enumerate(document["items"]):
            if not isinstance(item, dict):
                raise ValueError("items must contain objects")
            yield item, "/items/" + str(index)
    else:
        yield document, ""


def find_records(root, kind, query="", record_id=None, limit=10, offset=0):
    if not 1 <= limit <= 50 or offset < 0:
        raise ValueError("limit must be 1..50 and offset nonnegative")
    data = registry(root)
    if kind not in data["data_roots"]:
        raise ValueError("Unknown data kind")
    binding = data["data_roots"][kind]
    directory = inside(root, binding["path"])
    matches, issues = [], []
    root = Path(root).resolve()
    for path in sorted(directory.glob(binding["pattern"])) if directory.is_dir() else []:
        relative = path.relative_to(root).as_posix()
        try:
            resolved = inside(root, relative)
            if not resolved.is_file():
                continue
            document = json.loads(resolved.read_text(encoding="utf-8"))
            for item, pointer in records(document):
                item_id = next((item[k] for k in ("id", "product_id", "reference_id", "persona_id", "asset_id", "content_id", "lesson_id") if item.get(k) is not None), None)
                descriptor = {"id": item_id, "path": relative, "pointer": pointer}
                for key in ("name", "title", "display_name", "summary", "version", "status", "captured_at", "updated_at", "canonical_url", "source_url", "handle", "table_ids", "tags", "topics", "applicability"):
                    if key in item:
                        descriptor[key] = item[key]
                if record_id is not None and str(item_id) != record_id:
                    continue
                haystack = json.dumps(descriptor, ensure_ascii=False).casefold()
                if all(term in haystack for term in query.casefold().split()):
                    matches.append(descriptor)
        except (OSError, ValueError, TypeError) as exc:
            issues.append({"path": relative, "error_type": type(exc).__name__})
    return {
        "kind": kind, "storage_present": directory.is_dir(),
        "total_matches": len(matches), "offset": offset, "limit": limit,
        "results": matches[offset:offset + limit],
        "has_more": offset + limit < len(matches),
        "issue_count": len(issues), "issues": issues[:20],
        "note": "Metadata only; empty lookup is not proof no legacy/source data exists. Follow SOURCE-ROUTING and inspect relevant originals/unknown records.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    routed = sub.add_parser("route")
    routed.add_argument("skill")
    routed.add_argument("--task")
    routed.add_argument("--mode", choices=["product", "reference", "hybrid"])
    routed.add_argument("--hashes", action="store_true")
    lookup = sub.add_parser("find")
    lookup.add_argument("--kind", required=True)
    lookup.add_argument("--query", default="")
    lookup.add_argument("--id", dest="record_id")
    lookup.add_argument("--limit", type=int, default=10)
    lookup.add_argument("--offset", type=int, default=0)
    args = parser.parse_args()
    try:
        if args.command == "route":
            result = route(ROOT, args.skill, args.task, args.mode, args.hashes)
        else:
            result = find_records(ROOT, args.kind, args.query, args.record_id, args.limit, args.offset)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
