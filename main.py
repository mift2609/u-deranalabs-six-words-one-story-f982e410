#!/usr/bin/env python3
"""Six Words, One Story — deterministic entry writer.

Writes one complete six-word story to /output/entry.txt and verifies it:
exactly six words, 1-60 UTF-8 characters, non-blank.
"""
import os
import sys

STORY = "He planted orchards. She boarded planes."


def main() -> int:
    words = STORY.split()
    if len(words) != 6:
        print(f"error: story has {len(words)} words, expected 6", file=sys.stderr)
        return 1
    if STORY != STORY.strip():
        print("error: story has leading/trailing whitespace", file=sys.stderr)
        return 1
    encoded = STORY.encode("utf-8")
    if not 1 <= len(encoded) <= 60:
        print(f"error: story is {len(encoded)} bytes, expected 1-60", file=sys.stderr)
        return 1
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == STORY + "\n", "round-trip mismatch"
    print(f"wrote {out_path}: {STORY!r} ({len(words)} words, {len(encoded)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
