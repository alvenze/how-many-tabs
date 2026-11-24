"""How Many Tabs Do You Have Open? - make.fun entry.

Writes one number in digits and nothing else to /output/entry.txt:
843, an honest tab count. The kit's gate: UTF-8 text of 1 to 5
characters, not only white space; the judge wants exactly one number
in digits, no words, no punctuation, no second number.
"""

import os

ENTRY = "843"
OUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """The kit's gate: UTF-8 text of 1 to 5 characters, not only white
    space, and exactly one number in digits with nothing else."""
    assert 1 <= len(text) <= 5, "entry must be 1 to 5 characters"
    assert text.isdigit(), "entry must be digits only"
    assert text.strip(), "entry must not be only white space"


def main() -> None:
    check_gate(ENTRY)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check: re-read what was written and hold it to the gate again,
    # byte for byte, so a bad write can never pass silently.
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    check_gate(written)
    assert written == ENTRY, "written entry must match byte for byte"
    print(f"GATE OK: {len(written)} characters")


if __name__ == "__main__":
    main()
