#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261124.

Copies the front-page image held in this repository (entry.png) to
/output/entry.png. Pure Python 3 standard library, no network, no
randomness, no reading anything outside the repository: every run writes
the same bytes.

Run locally with:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))


if __name__ == "__main__":
    main()
