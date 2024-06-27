#!/usr/bin/python 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ["mango", "orange", "lemon", "pineapple", "cashew", "coconut"]
z = []
for i in x:
    print(i)
for i in range(len(y)):
    print(y[i])

[print(i) for i in x]

z = [i for i in y if i != "lemon"]
print(z)
k = [y[i] for i in range(len(y))]
print(k)

for i in x:
    if i > 5:
        print(i)
    else:
        print(f"{i} is not greater than 5")
j = [i if i != "mango" else "orange" for i in y]
print(j)

unsorted = [4, 3, 2, 0, 1, 9, 8, 7]
unsorted.sort()
print(unsorted)


m = x.copy()
print("Before changing", m)
x[5] = 12
print("after changing", m)
print()
print()
# --------------------- Tupple ------------------------
t = ("apple", "orange", "cherry")
print(t)
mytuple = ("mango",)
print(type(mytuple))
newlist = list(t)
newlist(1)

r = ()
for r in range[10]:
    print(r)







