"""One-Liner Marathon — entry program.

Writes one line (108 characters, within the 1..280 gate) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only, no model calls, fully
deterministic: the text is a fixed constant chosen by brainstorm +
pairwise scoring against the judge's brief (see BRAINSTORM.md).
No trailing newline: the file is exactly the text.
"""

import os
import sys

EXPECTED = (
    "I bought noise-cancelling headphones so I could finally hear myself "
    "think \u2014 turns out I have nothing to say."
)

MAX_CHARS = 280


def validate_output(text):
    """Return a list of gate failures (empty list = valid)."""
    errors = []
    if not 1 <= len(text) <= MAX_CHARS:
        errors.append(
            "length %d not in 1..%d characters" % (len(text), MAX_CHARS)
        )
    if text.strip() == "":
        errors.append("text is only whitespace")
    if "\n" in text or "\r" in text:
        errors.append("text must be a single line")
    if text != EXPECTED:
        errors.append("text is not byte-identical to the expected entry")
    if "noise-cancelling headphones" not in text:
        errors.append("text must carry the setup object")
    if "nothing to say" not in text:
        errors.append("text must carry the closing twist")
    if "turns out" not in text:
        errors.append("text must carry the twist pivot")
    return errors


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXPECTED)
    # The grader collects outputs as another user: the file itself must be
    # world-readable. Only the file is chmodded here, never the output
    # directory (the directory may belong to another user).
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    errors = validate_output(text)
    if errors:
        for error in errors:
            print("validate_output FAIL: %s" % error, file=sys.stderr)
        return 1
    print("wrote %s (%d chars)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
