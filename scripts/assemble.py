#!/usr/bin/env python3
import gzip
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "SwitchTVBox-0.4.19-standalone-test.nsp"
EXPECTED = "4b30466f34066f4f9894a5b91e803e00c549151ecb672b71964021c59fd827f5"
parts = sorted((ROOT / "payload").glob("*.part"))
assert parts, "No payload parts"
compressed = b"".join(p.read_bytes() for p in parts)
data = gzip.decompress(compressed)
assert len(data) == 38616280, "Wrong NSP size"
assert hashlib.sha256(data).hexdigest() == EXPECTED, "NSP checksum mismatch"
DEST.write_bytes(data)
print(f"Verified {DEST.name}: {len(data)} bytes, SHA-256 {EXPECTED}")
