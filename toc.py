#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ./toc.py hoge.md")
        sys.exit(0)


    # h1のみ
    with open(sys.argv[1], "r") as f:
        header = []
        for l in f:
            if l[0] == "#":
                header.append(l)
    # データ
    with open(sys.argv[1], "r") as f:
        data = f.read()


    with open(sys.argv[1].replace(".md", "")+"_with_toc.md", "w") as f:

        f.write("# 目次\n\n")
        for h in header:
            f.write("- ["+h.replace("# ", "").replace("\n", "")+"]("+h.replace("# ", "#").replace("\n", "").replace("(", "%28").replace(")", "%29")+")\n")

        f.write("\n")
        f.write(data)

    print("OK")

main()
