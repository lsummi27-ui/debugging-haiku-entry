"""Write a 5-7-5 haiku about debugging to /output/entry.txt.

The haiku:

    Midnight logs scroll past
    one red line blinks, then holds still
    it was a typo

Three lines, 17 syllables, 77 characters including the two newlines.
"""

import os

HAIKU = (
    "Midnight logs scroll past\n"
    "one red line blinks, then holds still\n"
    "it was a typo"
)


def main():
    # The sealed scorer requires 1-200 UTF-8 characters, not only
    # whitespace. Fail loudly here rather than shipping a bad entry.
    if not (1 <= len(HAIKU) <= 200) or not HAIKU.strip():
        raise ValueError("haiku is outside the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
