#!/usr/bin/env python3
"""The Worst Line an AI Could Say -- make.fun entry.

Writes a single pickup line (140 characters or fewer) to
/output/entry.txt and prints it.
"""

import os

ENTRY = "I ran 10,000 simulations of our first date. In 9,997, you said yes. The other three I deleted."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
