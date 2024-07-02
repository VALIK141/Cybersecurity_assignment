#!/usr/bin/python

import sys

def main():
    argv = sys.argv
    if len(argv) != 4:
        print("Error: usage ./filename x y z")
        return 0
    x = int(argv[1])
    y = int(argv[2])
    z = int(argv[3])
    largest = z
    if x > y:
        largest = x
    elif y > z:
        largest = y
    print(f"the largest numbe is {largest}")



if  __name__ == "__main__":
    main()

