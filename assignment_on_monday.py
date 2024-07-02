#!/usr/bin/python
import sys

def main():
    argv = sys.argv

    if len(argv) != 4:
        print("error: usage ./filename Asses1 Asses2 Exam")
        return -1

    Asses_1 = int(argv[1])
    Asses_2 = int(argv[2])
    Exam = int(argv[3])
    x = int(Asses_1 + Asses_2 + Exam)

    if x >= 70 and x <= 100:
        print("you are grade A")
    elif x >= 60 and x <= 69:
        print("you are grade B")
    elif x >= 50 and x <= 59:
        print("you are grade C")
    elif x >= 40 and x <= 49:
        print("you are grade D")
    elif x <= 39:
        print("you are grade F")
    else:
        print("Absent")



if __name__ == "__main__":
    main()
    


