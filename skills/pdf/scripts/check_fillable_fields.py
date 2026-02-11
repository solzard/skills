#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "pypdf",
# ]
# ///

import sys

from pypdf import PdfReader


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file.pdf>")
        return 1

    reader = PdfReader(sys.argv[1])
    if reader.get_fields():
        print("This PDF has fillable form fields")
    else:
        print(
            "This PDF does not have fillable form fields; you will need to visually "
            "determine where to enter data"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
