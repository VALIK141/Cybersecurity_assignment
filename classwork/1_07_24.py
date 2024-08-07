#!/usr/bin/python
import sys


def main():
    argv = sys.argv
    if len(argv) != 3:
        print("usage: ./filename x y")
        return 0 
    x = int(argv[1])
    y = int(argv[2])
    if x > y:
        print(f"{x} is greater than {y}")
    elif y > x:
        print(f"{y} is greater than {x}")
    elif x == y:
        print(f"{x} is equal to {y}")
    else:
        print("incorrect input")



if  __name__ == "__main__":
    main()

