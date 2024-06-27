#!/usr/bin/python

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ["bananana", "apple", "mango", "guavav", "pawpawpaw"]

print(len(x))
print(len(y)) 
print(type(x))
print(type(y))

print(x[1:4])
print(x[:3])
print(y[2:])
print(y[-2])
print("mango" in y)
if "lemon" not in y:
    print("lemon is not in the list y")
if "bananana" not in y:
    print("bananana is not in the list y")
y[4] = "lemon"
print(y)
if "lemon" in y:
    print("lemon is in the list y")

x.insert(2, 10)
print(x)
x.extend(y)
print(y)
x.extend(y)
print(x)
x.remove("bananana")
print(x)

for i in x:
    print(i)

for i in range(len(y)):
    print(y[i])

m = 0
while m <= len(x) -1:
    print(x[m])
    m += 1

[print(K) for K in y]





