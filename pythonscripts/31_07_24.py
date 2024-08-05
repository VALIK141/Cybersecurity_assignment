
from triangle import Triangle
from square import Square 
from animal import Animal
from human import Human
from dog import Dog

tri1 = Triangle(5, 4)
sqr1 = Square(6, 4)

print(tri1.area())
print(tri1.perimeter())
print(sqr1.area())
print(sqr1.perimeter())  

Helen = Human("Helen", "Oluchuchukwu", "Rice & Beans", "Pepsi")
Vahl = Human("Valentine", "Chidubem", "Beans and Bread", "Heineiken")
Esther = Human("Esther", "Mmesomachi", "Eba", "Malt")

print(Helen.drink())
print(Helen.eat())

print(Vahl.drink())
print(Vahl.eat())

print(Esther.drink())
print(Esther.eat())
print(Esther.lastname)

scoobie = Dog("Bone", "Milk and Blood")
Max = Dog("Dog food", "Serum")

print(Max.eat())
print(Max.drink())
print(scoobie.eat())
print(scoobie.drink()) 