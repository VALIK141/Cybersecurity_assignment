#!/usr/bin/python

for p in range (1,101):
    if p % 3 == 0:
        print("fizz")
    elif p % 5 == 0:
        print("buzz")
    elif p % 3 == 0 and p % 5 == 0:
        print("fizzbuzz")
    else:
        print(p)

