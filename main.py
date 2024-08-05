from student import Student
from lecturer import lecturer

student1 = Student("Emeka", "eze", "emeka@gmail.com", "emeka123", "LISTACC/CS/001", "Cyber security")
student2 = Student("Henry", "Nwafor", "henry@gmail.com", "henry123", "LISTACC/ML/00002")
lecturer1 = lecturer("Miracle", "sixtus", "miracle@gmail.com", "miracle123", "LIS020") 
lecturer2 = lecturer("councel", "okeke", "councel@)gmail.com", "councel123", "LISO30")


print(student1.getlogindetails())
print(student1.getstudentdetails())

print(student2.getlogindetails())
print(student2.getstudentdetails())

print(lecturer1.getlogindetails())
print(lecturer1.getlecturerdetails())

print(lecturer2.getlogindetails())
print(lecturer2.getlecturerdetails())
