#!/usr/bin/env python3
"""Restore the exact user attachments and verify them before publishing."""
import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist"
OUT.mkdir(exist_ok=True)
archive = b"".join(p.read_bytes() for p in sorted((ROOT / "release-payload/switchtvbox").glob("*.part")))
assert len(archive) == 37544135, "ZIP size mismatch"
assert hashlib.sha256(archive).hexdigest() == "dbfa0c6accef5b6759bff6351961baf4ab2b4a2f063adcd7408c163bfe7d2c33", "ZIP checksum mismatch"
(OUT / "SwitchTvbox.zip").write_bytes(archive)
with zipfile.ZipFile(OUT / "SwitchTvbox.zip") as z:
    assert z.testzip() is None, "Invalid ZIP"
    nro = z.read("switch/SwitchTVBox/SwitchTVBox.nro")
assert len(nro) == 38430485, "NRO size mismatch"
assert hashlib.sha256(nro).hexdigest() == "d00d3d336d8b89d82f45e49385fe4538378450e1651234c8dac0436eb10e8f2b", "NRO checksum mismatch"
(OUT / "SwitchTVBox.nro").write_bytes(nro)
print("Both original attachments restored and SHA-256 verified.")
