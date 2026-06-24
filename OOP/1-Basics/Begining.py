class Students:
    def __init__(self, name, age, section, FAFSA, gpa):
        self.name = name
        self.age = age
        self.section = section
        self.FAFSA = FAFSA
        self.gpa = gpa

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Section: {self.section}, FAFSA: {self.FAFSA}, GPA: {self.gpa}")

s = Students("John Doe", 20, "A", True, 3.5)
s.show()