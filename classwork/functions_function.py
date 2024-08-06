#!/usr/bin/python

import sys

def printstrcontent(str):
    [print(i) for i in str]

def revstr(str):
    i = len(str) - 1
    while i >= 0:
        print(str[i])
        i -= 1 

def main():
    argv = sys.argv
    if len(argv) != 2: 
        print("Error: usage; ./filename str")
        return -1
    str = argv[1]
    #printstrcontent(str)
    revstr(str)
    return 0

if __name__ == "__main__":
    main()

