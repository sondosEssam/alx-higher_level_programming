#!/usr/bin/python3
import hidden_4
stri = dir(hidden_4)
stri = sorted(i for i in stri if i[0:2] != "__")
if __name__ == "__main__":
    for i in stri:
        print("{}".format(i))
