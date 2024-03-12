#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = str((number))
m = ""if number >= 0 else "-"
r = (int(s[-1]))
r = r * -1 if number < 0 else r * 1
if r > 5:
    print(f"Last digit of {number} is {m}{s[-1]} and is greater than 5")
elif r == 0:
    print(f"Last digit of {number} is {m}{s[-1]} and is 0")
else:
    print(f"Last digit of {number} is {m}{s[-1]} and is less than 6 and not 0")
