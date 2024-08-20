class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,age,country,code):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.code=code

    def greet_student(self):
        greeting=f"Hello{self.first_name}, welcome to {self.school},your code is {self.code}"
        return greeting    
    
    def greet_by_age(self):
                greetings=f"Hello{self.first_name}, you were born in {2024-self.age}"
                return greetings
    
    def disp_initials(self):
          initials= {self.first_name[0]},{self.last_name[0]}
          return initials
    
    def disp_full_name(self):
          names= f"student names are {self.first_name} {self.last_name}"
          return names




        

