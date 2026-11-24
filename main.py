"""How Many Tabs Do You Have Open? - make.fun entry.

Writes one number in digits and nothing else to /output/entry.txt:
843, an honest tab count. The kit's gate: UTF-8 text of 1 to 5
characters, not only white space; the judge wants exactly one number
in digits, no words, no punctuation, no second number.
"""

import os

ENTRY = "843"

# The kit's gate, asserted inline: 1 to 5 characters, digits only,
# not only white space.
assert 1 <= len(ENTRY) <= 5, "entry must be 1 to 5 characters"
assert ENTRY.isdigit(), "entry must be digits only"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"GATE OK: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
