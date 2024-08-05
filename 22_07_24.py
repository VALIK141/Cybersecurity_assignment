
class Person:
    def __init__(self, fullname, phoneNumber):
        self.name = fullname
        self.phoneNumber = phoneNumber 

    def __str__(self):
        return f"{self.name} {self.phoneNumber}"
    
    def getname(self):
        return f"Hello, my name is {self.name}"
    


person1 = Person("Dubem","08063674247")
print(person1.name)
person1.name = "charles"
print(person1.phoneNumber)
print(person1)
print(person1.getname())

person2 = Person("Esther","09087909876")
print(person2) 
print(person2.phoneNumber)
print(person2.getname()) 

user1 =User("Martha" "Oba" "marthyartgmail.com", "marthy01010")
print(user1)
print(user1.greet())
print(user1.getloginsdetails())


