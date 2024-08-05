from lecturer import User 

class Student(User):
    def __init__(self, firstname, lastname, email, password, regno, department) -> None:
        super().__init__(firstname, lastname, email, password)
        self.regno = regno
        self.department = department

    def getregno(self):
        return self.regno
    
    def getstudentsdetails(self):
        return f" firstname: {self.firstname}\nlastname: {self.lastname}\nemail: {self.email}\npassword: {self.password}\nregno: {self.regno}\ndepartment: {self.department}"
    
    