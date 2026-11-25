"""Invent a Word We Need — entry program.

Writes a single invented word with its one-line definition to
/output/entry.txt. Deterministic: every run writes byte-identical output.
Standard library only, no network access.
"""

import os

ENTRY = (
    "Waveshame (n.): the embarrassment of waving back at "
    "someone who was waving at the person behind you."
)


def main() -> None:
    text = ENTRY
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not (1 <= len(text) <= 140):
        raise ValueError(
            "entry must be 1-140 characters, got %d" % len(text)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
