import json
class Student:
    def __init__(self,name):
        self.name=name
        self.courses=[] 
        self.attendance= {}
    
    def enroll(self,course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            self.attendance[course_name] =0 

class Institute:
    def __init__(self,file_name = "data.json"):
        self.file_name = file_name
        self.students= {} #key is student name and value is the student object itself
        self.courses= [] #total courses of institute
        self.load_data()

        #----------------------------------------------FILE HANDLING__________________________
       #save data
    def save_data(self):
        data= {
            "students":{ 
                name:{
                    "courses" : student.courses,
                    "attendance" : student.attendance

                }
                for name, student in self.students. items()
                }, #dict comprehension
            "courses": self.courses
        }
        with open(self.file_name, "w") as f:
            json.dump(data,f, indent=4)


#load data
    def load_data(self):
        try:
            with open(self.file_name, "r") as f:
                data= json.load(f)

                self.courses= data.get("courses, []") #data["courses"]

                
                for name, info in data.get("students", {}). items ():
                    student= Student(name) #object creation of student using composition
                    student.courses= info["courses"]
                    student.attendance= info["attendance"]
                    self.students[name]= student #dictionary of all students ijnobject from where key is student and value is student object
        except FileNotFoundError:
            self.students = {}
            self.courses= []

            #--------------------------------COURSE Management-----------------------------
            #adding course for institute
    def add_course(self,course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"Course added successively,  {course_name}")
        else:
            print("Course Already exists.")

        #--------------------------------------------STUDENT Management----------------------
    def add_student(self,student_name): 
        if students_name not in self.students:
            self.students[student_name]=Student(student_name) #object creation
            print(f"Student added: {student-name}")
        else:
            print("Student already exists.")

    

            



        