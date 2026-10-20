"""Verify the portable handoff ZIP against its manifest, without extraction."""
import hashlib
import json
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "handoff/CONTENTS.json").read_text(encoding="utf-8"))
archive = root / manifest["archive"]
assert hashlib.sha256(archive.read_bytes()).hexdigest() == manifest["sha256"], "ZIP hash mismatch"
with ZipFile(archive) as bundle:
    assert len(bundle.namelist()) == len(set(bundle.namelist())), "Duplicate ZIP paths"
    assert set(bundle.namelist()) == {f["path"] for f in manifest["files"]}, "ZIP coverage mismatch"
    for item in manifest["files"]:
        path = PurePosixPath(item["path"])
        assert not path.is_absolute() and ".." not in path.parts and ":" not in item["path"], "Unsafe ZIP path"
        assert path.parts[0] in {".errare", "media"}, "Unexpected root"
        data = bundle.read(item["path"])
        assert len(data) == item["bytes"], "Size mismatch: " + item["path"]
        assert hashlib.sha256(data).hexdigest() == item["sha256"], "Hash mismatch: " + item["path"]
print(f"Verified {len(manifest['files'])} runtime/media files; no extraction performed.")
