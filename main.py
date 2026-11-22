#!/usr/bin/env python3
"""Entrypoint for the make.fun news-image-20261122 entry.

The repository ships the finished front page as ``entry.png`` (drawn at
build time with Pillow from the day's reporting; see build_image.py in
the task folder, not part of the entry). All this program does is copy
that image, byte for byte, to the output directory the harness gives
it, and then prove the copy is identical before it reports success.

Standard library only, no network, no clock, no randomness: the same
input bytes always produce the same output bytes.
"""

import hashlib
import os
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
MAX_IMAGE_BYTES = 1_048_576  # competition gate: at most 1 MiB


def sha256_hex(data: bytes) -> str:
    """Hex digest of a byte string, used to compare source and copy."""
    return hashlib.sha256(data).hexdigest()


def fail(message: str) -> int:
    """Report a fatal problem on stderr and return a nonzero status."""
    print(f"error: {message}", file=sys.stderr)
    return 1


def main() -> int:
    repo_root = Path(__file__).resolve().parent
    source_path = repo_root / IMAGE_NAME

    if not source_path.is_file():
        return fail(f"missing {IMAGE_NAME} next to {__file__}")

    try:
        image_bytes = source_path.read_bytes()
    except OSError as exc:
        return fail(f"cannot read {source_path}: {exc}")

    if not image_bytes.startswith(b"\x89PNG"):
        return fail(f"{IMAGE_NAME} is not a PNG file")

    if len(image_bytes) > MAX_IMAGE_BYTES:
        return fail(f"{IMAGE_NAME} is {len(image_bytes)} bytes, over the "
                    f"{MAX_IMAGE_BYTES} byte limit")

    source_digest = sha256_hex(image_bytes)

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR",
                                     DEFAULT_OUTPUT_DIR))
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        return fail(f"cannot create output directory {output_dir}: {exc}")

    target_path = output_dir / IMAGE_NAME
    try:
        target_path.write_bytes(image_bytes)
        written_bytes = target_path.read_bytes()
    except OSError as exc:
        return fail(f"cannot write {target_path}: {exc}")

    if sha256_hex(written_bytes) != source_digest:
        return fail(f"{target_path} differs from {source_path} "
                    f"(sha256 mismatch)")

    print(f"wrote {target_path} ({len(written_bytes)} bytes, "
          f"sha256 {source_digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
