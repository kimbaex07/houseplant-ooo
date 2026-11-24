"""The Houseplant Out-of-Office (u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047).

Writes the entry line from entry.txt (next to this script) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default "output/").

The entry is one out-of-office auto-reply, 120 characters or fewer,
written as if a houseplant sent it.

Normalization: a single trailing newline (and a preceding carriage
return, i.e. one "\r\n" line ending) that an editor may have added is
dropped before validation, so the graded line is exact.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    with open(src, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    # Drop at most one trailing newline an editor may have added:
    # one "\n", then one "\r" if it preceded it (a "\r\n" ending).
    if text.endswith("\n"):
        text = text[:-1]
    if text.endswith("\r"):
        text = text[:-1]
    if not (1 <= len(text) <= 120):
        print("entry must be 1-120 characters, got %d" % len(text), file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output/")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(dst, 0o644)
    print("wrote %s (%d characters)" % (dst, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
