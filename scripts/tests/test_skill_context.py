"""Offline routing/lookup regression checks. No model or external account calls."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("skill_context", ROOT / "scripts/skill_context.py")
CTX = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CTX)


class SourceRoutingTests(unittest.TestCase):
    def test_product_does_not_require_reference(self):
        result = CTX.route(ROOT, "er-video", "prompts", "product")
        paths = [x["path"] for x in result["sources_to_open"]]
        self.assertIn("01-Brand/PRODUCT-SOURCES.md", paths)
        self.assertIn("01-Brand/product-sources.json", paths)
        self.assertNotIn("02-Research/SOCIAL-RESEARCH.md", paths)
        self.assertNotIn("reference", result["lookup_kinds"])
        self.assertEqual(len(paths), len(set(paths)))

    def test_hybrid_keeps_both_sources(self):
        paths = [x["path"] for x in CTX.route(ROOT, "er-video", "prompts", "hybrid")["sources_to_open"]]
        self.assertIn("01-Brand/PRODUCT-SOURCES.md", paths)
        self.assertIn("02-Research/SOCIAL-RESEARCH.md", paths)

    def test_caption_does_not_reload_concept_or_model(self):
        result = CTX.route(ROOT, "er-video", "caption", "hybrid")
        paths = [x["path"] for x in result["sources_to_open"]]
        self.assertIn("00-Standards/CAPTION.md", paths)
        self.assertNotIn("02-Research/SOCIAL-RESEARCH.md", paths)
        self.assertNotIn("02-Research/MODELS.md", paths)
        self.assertEqual(result["lookup_kinds"], ["production", "profile"])

    def test_source_mode_cannot_be_guessed_by_helper(self):
        with self.assertRaises(ValueError):
            CTX.route(ROOT, "er-video", "prompts")

    def test_unsupported_tasks_fail_closed(self):
        with self.assertRaises(ValueError):
            CTX.route(ROOT, "er-video", "publish", "product")
        with self.assertRaises(ValueError):
            CTX.route(ROOT, "missing-skill")

    def test_every_declared_task_has_existing_sources(self):
        for skill, entry in CTX.registry(ROOT)["skills"].items():
            for task, plan in entry["tasks"].items():
                modes = ["product", "reference", "hybrid"] if plan.get("include_mode_sources") else [None]
                for mode in modes:
                    with self.subTest(skill=skill, task=task, mode=mode):
                        result = CTX.route(ROOT, skill, task, mode)
                        self.assertTrue(result["sources_to_open"])


class MetadataTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="er-skill-tests-")
        self.root = Path(self.temp.name).resolve()
        (self.root / "00-Standards").mkdir()
        registry = {"data_roots": {"product": {"path": ".errare/library/products", "pattern": "**/*.json"}}}
        (self.root / "00-Standards/skills.json").write_text(json.dumps(registry), encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, value):
        folder = self.root / ".errare/library/products"
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / name
        path.write_text(json.dumps(value), encoding="utf-8")
        return path

    def test_missing_runtime_is_explicit_and_not_created(self):
        result = CTX.find_records(self.root, "product")
        self.assertFalse(result["storage_present"])
        self.assertEqual(result["results"], [])
        self.assertFalse((self.root / ".errare").exists())

    def test_lookup_paginates_and_retains_versions(self):
        self.write("a.json", {"items": [{"id": "P", "name": "Home plan", "version": "1"}, {"id": "P", "name": "Home plan", "version": "2"}]})
        result = CTX.find_records(self.root, "product", "home", limit=1)
        self.assertEqual(result["total_matches"], 2)
        self.assertTrue(result["has_more"])
        self.assertEqual(result["results"][0]["pointer"], "/items/0")
        following = CTX.find_records(self.root, "product", record_id="P", limit=1, offset=1)
        self.assertEqual(following["results"][0]["version"], "2")

    def test_lookup_does_not_echo_full_private_payload(self):
        self.write("a.json", {"id": "P", "name": "Home", "private_notes": "SHOULD_NOT_APPEAR"})
        result = CTX.find_records(self.root, "product")
        self.assertNotIn("SHOULD_NOT_APPEAR", json.dumps(result))

    def test_malformed_record_is_reported_not_silently_missing(self):
        self.write("a.json", {"items": "wrong-type"})
        result = CTX.find_records(self.root, "product")
        self.assertEqual(result["issue_count"], 1)
        self.assertEqual(result["total_matches"], 0)

    def test_traversal_and_invalid_pagination_rejected(self):
        with self.assertRaises(ValueError):
            CTX.inside(self.root, "../outside")
        with self.assertRaises(ValueError):
            CTX.find_records(self.root, "product", limit=0)
        with self.assertRaises(ValueError):
            CTX.find_records(self.root, "product", offset=-1)


if __name__ == "__main__":
    unittest.main()
