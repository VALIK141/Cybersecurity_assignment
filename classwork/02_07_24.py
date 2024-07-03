#!/usr/bin/python

f = 'met, mine, eat'
#[print(i) for i in f]
#print(f[::-1])
y = len(f) - 1
while y >= 0:
    print(f[y])
    y -= 1

def myfunction():
    print("first of functions")
def myfunction(str):
    return str

def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
def exp(a, b):
    return a ** b

def solve(a, b):
# return  mult(mult(div(a, b), div(b, a)), a)

 def solve(a, b):
     return sum(div(div(exp(a, b), b, div(exp(b, a), a), b)), div(a, b))
 print(solve(2, 3))





