#!/usr/bin/python

myset = {"banana", "mango", "apple", "orange", "pineaple", True, 1, 2}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
x = [10, 11, 13, 14, 10]
y = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
#myset.update(set2) 
#myset.update(x)
#[myset.remove("mango") if "mango" in myset else print("mango not in the set")]
#for i in myset:
#    print(i)
#set3 = myset.union(set2, x, y)
#set 3 = set2 & y
#set2.intersection_update(y)
#set3 = y.dieference(set2)
set3 = set2.symmetric_difference(y)
print(set3)





myDict = (
        {
        "name": "Helen",
        "age": 15,
        "institution": "EBSU",
        "Graduationyear": 2023,
        "isStudent": False,
        "skill": ["HTML", "CSS", "JSS", "C#", "JAVA", "PYTHON"] 
        }
print(myDict["skill"])
print(myDict.keys())
print(myDict.values())
print(myDict.items())
[print(myDict["age"]) if "age" in myDict else print("age is not in my Dict")]

del myDict["age"] 
print(myDict)
myDict["age"] = 15
print(myDict)

for x in myDict:
    print






    

