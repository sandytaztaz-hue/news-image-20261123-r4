#!/usr/bin/env python3
"""Sum 23 R4 entry runner (standard library only).

Copies the shipped entry.png to the output entry.png byte-for-byte and
verifies the copy's SHA-256 against the hash baked into this program.
The output directory comes from MAKEFUN_OUTPUT_DIR, falling back to
/output when that variable is absent. Exits non-zero on any mismatch.
"""
import hashlib
import os
import shutil
import sys

EXPECTED_SHA256 = "7eee5b44b5fc086e680874af190d4b07b638516349a25c752527a5650733493c"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    digest = hashlib.sha256(open(dst, "rb").read()).hexdigest()
    if digest != EXPECTED_SHA256:
        print("SHA-256 mismatch: got %s, expected %s" % (digest,
              EXPECTED_SHA256), file=sys.stderr)
        return 1
    print("entry.png written to %s (sha256 %s, %d bytes)"
          % (dst, digest, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
