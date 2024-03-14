#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ar = sys.argv
    j = len(ar)
    print("{} argument{}".format(j - 1, "s" if j != 2 else ""), end="")
    print("{}".format("." if j == 1 else ":"))
    if len(ar) > 1:
        for i in range(1, len(ar)):
            print("{}: {}".format(i, ar[i]))
