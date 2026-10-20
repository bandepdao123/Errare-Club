"""Read-only seed, routing, template and documentation checks.

This is not an executable creative dispatcher or a production/publishing gate.

Run from any directory with Python 3.11+. Standard library only.
"""

import json
import re
import sys
from pathlib import Path
from uuid import UUID

ROOT = Path(__file__).resolve().parents[1]
errors = []
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        errors.append(message)


def load_registry(filename, expected):
    path = ROOT / "01-Brand" / filename
    data = json.loads(path.read_text(encoding="utf-8"))
    check(data["schema_version"] == "0.1.0", f"{filename}: version")
    check(data["source_id"] == "EC-WORLD", f"{filename}: provenance")
    check(data["source_status"] == "source_stated_unverified", f"{filename}: source status")
    items = data["items"]
    check(len(items) == expected, f"{filename}: expected {expected} seed records")
    ids = [x["id"] for x in items]
    check(len(ids) == len(set(ids)), f"{filename}: duplicate ID")
    return {x["id"]: x for x in items}


def validate():
    cast = load_registry("cast.json", 8)
    tables = load_registry("tables.json", 10)
    products = load_registry("products.json", 10)
    locations = load_registry("locations.json", 16)
    for cid, person in cast.items():
        try:
            UUID(person["soul_id"])
        except (ValueError, TypeError, KeyError):
            check(False, f"{cid}: invalid source Soul UUID")
        else:
            check(True, f"{cid}: Soul UUID syntax")
        check(bool(person["soul_hint"]), f"{cid}: missing hint")
        check(person["soul_availability"] == "not_checked", f"{cid}: unverified availability")
        for key in ("character_sheet_asset_id", "turnaround_asset_id", "expression_sheet_asset_id"):
            check(person[key] is None, f"{cid}: seed incorrectly claims imported {key}")
        for tid in person["table_ids"]:
            check(tid in tables, f"{cid}: missing Table {tid}")
    check(len({p["soul_id"] for p in cast.values()}) == len(cast), "duplicate source Soul UUID")
    for tid, table in tables.items():
        for cid in table["primary_cast_ids"]:
            check(cid in cast, f"{tid}: missing cast {cid}")
            if cid in cast:
                check(tid in cast[cid]["table_ids"], f"{tid}: inverse cast membership")
        for pid in table["product_ids"]:
            check(pid in products, f"{tid}: missing design {pid}")
            if pid in products:
                check(products[pid]["table_id"] == tid, f"{pid}: wrong Table")
    for pid, product in products.items():
        check(product["table_id"] in tables, f"{pid}: missing Table")
        check(product["display_name"] == " ".join(product["print_text"].splitlines()), f"{pid}: print/name mismatch")
        check(product["identity_kind"] == "source_design_code_not_verified_sku", f"{pid}: source ID claim")
        for key in ("artwork_asset_id", "store_product_id", "sku", "landing_url", "price", "currency", "verified_at", "print_placement"):
            check(product[key] is None, f"{pid}: seed incorrectly claims known {key}")
        check(product["availability"] == "unknown", f"{pid}: unknown stock")
    for lid, loc in locations.items():
        for cid in loc["cast_ids"]:
            check(cid in cast, f"{lid}: missing cast {cid}")
        if loc["table_id"] is not None:
            check(loc["table_id"] in tables, f"{lid}: missing Table")
        if loc["product_id"] is not None:
            check(loc["product_id"] in products, f"{lid}: missing design")
            if loc["product_id"] in products:
                check(products[loc["product_id"]]["table_id"] == loc["table_id"], f"{lid}: design/Table mismatch")
        check(loc["timezone"] == "America/New_York", f"{lid}: scene timezone")
        check(loc["plate_asset_id"] is None and loc["plate_rights"] == "not_checked", f"{lid}: unverified plate")
        if loc["source_coverage"] == "full_slot":
            check(all(loc[k] for k in ("lighting", "source_error_options", "red_prop")), f"{lid}: incomplete full slot")
    partial = [x["id"] for x in locations.values() if x["source_coverage"] != "full_slot"]
    check(partial == ["loc-reply-all"], "15 full slots plus linked partial Reply All")
    config = json.loads((ROOT / "00-Standards/entrypoints.json").read_text(encoding="utf-8"))
    check(config["status"] == "design_only_not_executable_dispatcher", "routing implementation status")
    check(config["schema_version"] == "0.1.4", "routing contract version")
    expected_modes = {"product": {"product"}, "reference": {"reference"}, "hybrid": {"product", "reference"}}
    check(set(config["entry_modes"]) == set(expected_modes), "entry mode set")
    for mode, expected in expected_modes.items():
        entry = config["entry_modes"][mode]
        required_kinds = entry["required_source_kinds"]
        optional_kinds = entry["optional_source_kinds"]
        check(set(required_kinds) == expected, f"{mode}: independent required sources")
        check(len(required_kinds) == len(set(required_kinds)), f"{mode}: duplicate required source")
        check(not set(required_kinds).intersection(optional_kinds), f"{mode}: required/optional overlap")
        check(set(optional_kinds).issubset({"product", "reference"}), f"{mode}: invalid optional source")
    check(config["default_campaign_required"] is False, "standalone Content must not require Campaign")
    check(set(config["formats"]) == {"photo_post", "video"}, "two output packages")
    check(config["layouts"] == {"photo_post": ["single", "carousel"]}, "carousel is a photo post layout")
    check(set(config["tasks"]) == {"concept", "prompts", "generate", "review", "revision", "caption", "close"}, "task/source separation")
    routing_paths = [config[k] for k in ("shared_workflow", "output_contract", "production_guide", "model_guide", "media_contract", "source_routing", "skills_proposal", "audience_guide", "visual_guide")]
    media = json.loads((ROOT / config["media_contract"]).read_text(encoding="utf-8"))
    check(media["schema_version"] == config["schema_version"], "media/routing version agreement")
    check(set(media["packages"]) == {"photo_post", "video"}, "media package set")
    caption = media["caption_policy"]
    check(caption["locale"] == "en-US", "caption locale")
    check(caption["hashtag_min"] == 3 and caption["hashtag_max"] == 5, "caption hashtag range")
    check(caption["hashtags_storage"] == "separate_array_render_once_after_body", "hashtag storage")
    photo = media["packages"]["photo_post"]
    check(photo["required_deliverables"] == ["image_exports", "caption"], "photo post deliverables")
    check(photo["completion_requires_actual_images"] is True, "photo package must deliver actual images")
    check(photo["export_targets"] == "selected_platform_placement_profiles" and photo["all_possible_sizes_required"] is False, "scoped image export targets")
    video = media["packages"]["video"]
    check(video["required_deliverables"] == ["frame_pair_prompt", "video_prompt", "caption"], "video three-part frame-pair prompt package")
    pair = video["frame_pair"]
    check(pair["shared_prompt_count"] == 1 and pair["separate_image_outputs"] == 2, "one shared prompt requests two separate frames")
    check(pair["output_layout"] == "separate_files_not_collage", "frame pair output layout")
    check(pair["first_time_s"] == 0 and pair["last_time_source"] == "duration_s", "first t0 / last duration rule")
    check(pair["duration_required_for_final_package"] is True and pair["roles"] == ["first", "last"], "duration and role requirements")
    check(video["actual_frame_pair_images_required"] is False and video["actual_video_required"] is False, "video package must not imply rendering")
    audience = media["audience_policy"]
    check(audience["market"] == "US" and audience["locale"] == "en-US", "project audience/locale")
    check(audience["scope"] == "all_audience_facing_content_and_creative", "US audience applies beyond caption")
    visual = media["visual_policy"]
    check(visual["default_style"] == "everyday_smartphone" and visual["video_camera"] == "human_handheld_phone", "phone-life/handheld defaults")
    check(visual["cinematic_requires_explicit_request"] is True, "cinematic requires request")
    image_tool = media["image_generation"]
    check(image_tool["tool"] == "image_gen" and image_tool["runtime"] == "codex_builtin" and image_tool["external_provider_fallback"] is False, "Codex built-in ImageGen only")
    routing_paths += [audience["guide"], visual["guide"]]
    routing_paths += [caption["voice_guide"], media["output_guide"], media["source_routing"], media["skills_proposal"]]
    routing_paths += [entry["guide"] for entry in config["entry_modes"].values()]
    routing_paths += list(config["templates"].values())
    for rel in routing_paths:
        resolved = (ROOT / rel).resolve()
        check(resolved.is_relative_to(ROOT) and resolved.is_file(), f"routing path missing/outside workspace: {rel}")
    for name in ("content", "attempt"):
        template = json.loads((ROOT / config["templates"][name]).read_text(encoding="utf-8"))
        check(template["is_template"] is True and template["id"] is None, f"{name}: template must not allocate ID")
        check(template["schema_version"] == config["schema_version"], f"{name}: contract version")
        if name == "content":
            check(all(template[k] is None for k in ("entry_mode", "task", "format", "campaign_id", "current_attempt_id", "selected_master_ref")), "content template must not imply selected source/roster/master")
            check(template["source_refs"] == [] and template["persona_refs"] == [], "content template must not invent inputs/persona")
            check(template["duration_s"] is None and template["frame_plan"] is None and template["visual_override_ref"] is None, "template must not invent duration, frame pair or cinematic permission")
        else:
            check(template["actual_inputs"] is None and template["actual_model"] == "unknown", "attempt template must not invent tool provenance")
            check(template["output_text_ref"] is None and template["output_asset_ids"] == [], "attempt template must not invent outputs")
            check(template["provider_job_id"] is None and template["review_refs"] == [], "attempt template must not invent render/review")
    required = [
        "README.md", "AGENTS.md", "SYSTEM.md", "01-Brand/BRAND.md",
        "00-Standards/workflow.md", "00-Standards/quality.md", "00-Standards/contracts.md",
        "00-Standards/storage-and-recovery.md", "02-Research/SOURCES.md", "02-Research/NATURE-STUDIO.md",
        "03-Campaigns/README.md", "04-Productions/README.md", "05-Distribution/README.md",
        "06-Insights/MEASUREMENT.md", "07-Operations/ROADMAP.md", "07-Operations/decisions.md",
        "08-Evaluation/QA.md",
        "07-Operations/SCOPE.md", "02-Research/SOCIAL-RESEARCH.md", "01-Brand/WEBSITE-REFERENCE.md",
        "02-Research/INTAKE.md", "02-Research/MODELS.md", "04-Productions/OUTPUT-CONTRACT.md",
        "04-Productions/templates/brief.md", "04-Productions/templates/concept.md", "04-Productions/templates/SUMMARY.md",
        "00-Standards/CAPTION.md", "00-Standards/SOURCE-ROUTING.md", "07-Operations/SKILLS.md",
        "00-Standards/US-AUDIENCE.md", "00-Standards/PHONE-MEDIA.md",
        "01-Brand/PRODUCT-SOURCES.md",
    ]
    for rel in required:
        check((ROOT / rel).is_file(), f"missing document: {rel}")
    skill_registry = json.loads((ROOT / config["skills_registry"]).read_text(encoding="utf-8"))
    expected_skills = {"er-sanpham", "er-nghiencuu", "er-taoanh", "er-video", "er-kiemmedia", "er-dongmedia", "er-quanlykenh"}
    check(set(skill_registry["skills"]) == expected_skills, "seven er-prefixed skills")
    check(media["skills_registry"] == config["skills_registry"], "shared skill registry")
    for name, entry in skill_registry["skills"].items():
        skill_file = (ROOT / entry["path"]).resolve()
        check(skill_file.is_relative_to(ROOT) and skill_file.is_file(), f"{name}: skill file")
        check((skill_file.parent / "agents/openai.yaml").is_file(), f"{name}: UI metadata")
        check(entry["default_task"] in entry["tasks"], f"{name}: default task exists")
        required.append(entry["path"])
        for task, plan in entry["tasks"].items():
            for kind in plan["data_kinds"]:
                check(kind in skill_registry["data_roots"], f"{name}/{task}: unknown lookup kind")
            for rel in skill_registry["common_sources"] + plan["sources"]:
                path = (ROOT / rel).resolve()
                check(path.is_relative_to(ROOT) and path.is_file(), f"{name}/{task}: missing/outside source {rel}")
    for rel in required:
        path = ROOT / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            resolved = (path.parent / local).resolve()
            check(resolved.is_relative_to(ROOT), f"{rel}: link outside workspace: {target}")
            check(resolved.exists(), f"{rel}: broken local link: {target}")
    print(f"Checks: {checks}; failures: {len(errors)}")
    print("Seed: 8 cast; 10 Tables; 10 source designs; 15 full location slots + 1 partial linked scene.")
    for error in errors:
        print(f"FAIL: {error}")
    print("Scope: seed/source routing, packages, frame-pair timing rule, US/phone/tool policies, templates and links.")
    print("Not checked: skill execution, native audience fit, actual two-image tool support/continuity or video QA.")
    return 1 if errors else 0


if __name__ == "__main__":
    try:
        sys.exit(validate())
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"FAIL: invalid/incomplete bundle: {exc}")
        sys.exit(1)
