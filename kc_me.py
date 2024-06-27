#!/usr/bin/python

for j in range(50):
    print(j)


numbers = list(range(1, 50))
even_numbers = [] 
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num) 
print(even_numbers) 


