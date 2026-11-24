"""Two Days of Quiet Dread — make.fun entry.

Writes one code review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread. The judge picks the funnier comment in pairs, weighing
most: single-line approval with quiet dread; funny on the first read with
the laugh coming from the dread itself; dread kept quiet by understatement
and a flat tone; reading like a comment a tired engineer would really paste
before clicking approve; a fresh turn of phrase.

The line chosen here works the dread out of the universe itself, stated
flatly as a scheduling fact: everything passes, nothing is broken, and the
heat death of the universe remains on schedule. The approval is real
("LGTM", "Ship it"), the dread is quiet (no exclamation, no melodrama),
and the laugh comes from the dread, not from a joke bolted onto it.
"""

import os
import sys

# The entry: one line, approves the PR, carries quiet existential dread.
LINE = (
    "LGTM. Everything passes, nothing is broken, and the heat death "
    "of the universe remains on schedule. Ship it."
)

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text):
    """Mirror the house gate: UTF-8 text of 1 to 140 characters, not only
    white space, a single line."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= 140):
        raise ValueError("entry is %d characters, gate needs 1-140" % len(text))
    if not text.strip():
        raise ValueError("entry is only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8
    # The judge's first criterion: the comment must actually approve.
    lowered = text.lower()
    if not any(word in lowered for word in ("lgtm", "approved", "approve", "ship it", "merging")):
        raise ValueError("entry carries no approval")
    return True


def main():
    check_gate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Read it back and re-verify, so what the grader reads is what we gated.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    check_gate(written)
    if written != LINE:
        raise ValueError("round-trip mismatch")
    print("wrote %d chars to %s" % (len(written), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
