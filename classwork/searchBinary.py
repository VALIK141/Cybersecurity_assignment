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
    left = 0
    right = len(array) - 1
    while left <= right:
        if array[left] != array[right]:
            return False
        left =+ 1
        right -+ 1
    return True
