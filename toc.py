#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import string

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
            link = "("+h.replace("# ", "#").replace("\n", "").replace("(", "").replace(")", "").replace(" ", "-").lower()+")\n"
            link = link.translate(str.maketrans("", "", string.punctuation))
            f.write("- ["+h.replace("# ", "").replace("\n", "")+"]"+link)

        f.write("\n")
        f.write(data)

    print("OK")

main()
