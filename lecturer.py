from an _22_07_24 import user

class lecturer(user):
    def __init__(self, firstname, lastname, email, password, staffId):
        super().__init__(firstname, lastname, email, password)
        self.staffId = staffId

    def getstaffId(self):
        return self.staffId
    
    def getlecturerdetails(self):
        return f" firstname: {self.firstname}\n: {self.lastname}\nemail: {self.email}\npassword: {self.password}\nstaffId: {self.staffId}"
    