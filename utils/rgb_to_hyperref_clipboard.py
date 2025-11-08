#!/usr/bin/env python3

import sys
import os


def main():
    if len(sys.argv) != 2:
        print("Usage: rgb_to_hyperref.py <rgb>")
        sys.exit(1)

    rgb = map(
        lambda x: "{:.3}".format(int(x, 16) / 255.0),
        [sys.argv[1][0:2], sys.argv[1][2:4], sys.argv[1][4:6]],
    )
    value = " ".join(rgb)
    os.system(f"echo -n '{value}' | xclip -selection clipboard")
    print(f"Copied {value} to clipboard")


if __name__ == "__main__":
    main()
