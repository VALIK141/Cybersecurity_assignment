#!/usr/bin/python 

def newlist(my_list):
    i = 0
    for i in my_list:
        print(i)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)


def findsum(arr, target):
    i = 0
    while i < len(arr): 
        j = i + 1
        while j < len(arr):
            if arr[i] + arr[j] == target:
                return [i, j]
            j += 1
        i += 1
    return -1
x = [1, 3, 4, 5, 9, 10, 14, 16]
print(findsum(x, 9))

newlist = [1, 2, 3, 4, 5]
print(newlist)


def factorialwithloop(x):
    sum = 1
    i = 1
    while i <= x:
        sum *= i
        i += 1
    return sum

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x - 1))

print(factorial(5))

