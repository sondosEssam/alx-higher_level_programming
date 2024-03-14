#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ar = sys.argv
    j = 0
    if len(ar) > 1:
        for i in range(1, len(ar)):
            j += int(ar[i])
    print(j)
