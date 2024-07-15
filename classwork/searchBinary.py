#!/usr/bin/python

def Binarysearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        potentialmatch = arr[middle]
        if target == potentialmatch:
            return middle
        elif target < potentialmatch:
            right = middle - 1
        elif target > potentialmatch:
            left = middle + 1
    return - 1
Grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(Binarysearch(Grades, 5))


#palindromes


def determinepalindrome(array):
    start = 0
    End = len(array) - 1
    while start <= End:
        if array[start] != array[End]:
            return False
        start += 1
        End =+ 1
    return true
print(determinepalindrome("NICHOLAS"))

