class School:
    name= "Vidyajyoti school"
    estd= 1920
    def __init__(self,students,location,branch):
        self.students=students
        self.location=location
        self.branch=branch
    
    def show_info(self):
        print(f" My school has {self.students} students, located at {self.location} and it has {self.branch} branch")
   
    @classmethod
    def change_name (cls,name,estd):
        cls.name=name
        cls.estd= estd

    @staticmethod
    def change():
        print("It is changed")
        
s1=School(1200,"Bkt",False)
s1.show_info()

School.change_name("Amar Jyoti",1955)
School.change()