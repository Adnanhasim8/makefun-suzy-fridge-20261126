"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line to /output/entry.txt (UTF-8, no network).
Python 3.13 standard library only.
"""

import os

ENTRY = "My fridge hums at 3 a.m., gossiping about me to the milk."


def main() -> None:
    # Gate assertions: the entry must be exactly one line, 1-200 chars, non-empty.
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was written, not just what was intended.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from ENTRY"
    assert "\n" not in written and 1 <= len(written) <= 200, "written entry fails gate"


if __name__ == "__main__":
    main()
