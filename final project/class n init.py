# ============================================================
# CONCEPT: class + __init__
# WHY: A class is a blueprint. __init__ runs automatically
#      the moment you create an object from that blueprint.
# ============================================================

# --- WITHOUT a class (repetitive, messy) ---
student1_name = "Pravat"
student1_courses = []
student1_attendance = {}

student2_name = "Asha"
student2_courses = []
student2_attendance = {}
# Problem: 3 variables per student. 100 students = 300 variables. Chaos.

print("WITHOUT class:")
print(student1_name, student1_courses, student1_attendance)


# --- WITH a class (clean blueprint) ---
class Student:
    def __init__(self, name):   # runs automatically on creation
        self.name = name        # THIS student's name
        self.courses = []       # THIS student's courses (fresh list each time)
        self.attendance = {}    # THIS student's attendance (fresh dict each time)

# Creating objects from the blueprint
s1 = Student("Pravat")   # __init__ fires here automatically
s2 = Student("Asha")     # __init__ fires here automatically

print("\nWITH class:")
print(s1.name, s1.courses, s1.attendance)
print(s2.name, s2.courses, s2.attendance)

# --- Proof that each object is independent ---
s1.courses.append("Math")
print("\nAfter adding Math to s1 only:")
print("s1 courses:", s1.courses)   # ['Math']
print("s2 courses:", s2.courses)   # []  <-- unaffected

# ============================================================
# WHAT self IS:
#   self = the specific object being created right now
#   When you write Student("Pravat"), Python passes that new
#   object in as self automatically. You never pass it yourself.
#
#   self.name = name  means: attach 'name' to THIS object
#   Without self, name would just be a local variable
#   that disappears when __init__ finishes.
# ============================================================

# --- Seeing self in action ---
class StudentVerbose:
    def __init__(self, name):
        print(f"  __init__ fired! self is: {id(self)}")  # unique memory address
        self.name = name

print("\nCreating two students, watch __init__ fire:")
x = StudentVerbose("Pravat")
y = StudentVerbose("Asha")
print(f"  x lives at: {id(x)}")   # same address as self when x was created
print(f"  y lives at: {id(y)}")   # different address

# ============================================================
# CONCEPT: Instance attributes and self
# WHY: Each object needs its OWN copy of data.
#      self is what makes that happen.
# ============================================================

class Student:
    def __init__(self, name):
        self.name = name        # instance attribute
        self.courses = []       # instance attribute
        self.attendance = {}    # instance attribute

# --- Create two separate students ---
s1 = Student("Pravat")
s2 = Student("Asha")

# Each student has their OWN name
print(s1.name)   # Pravat
print(s2.name)   # Asha

# --- Prove data is ISOLATED per object ---
s1.courses.append("Math")
s1.courses.append("Physics")
s2.courses.append("English")

print(s1.courses)   # ['Math', 'Physics']  -- s2 not affected
print(s2.courses)   # ['English']          -- s1 not affected

# ============================================================
# WHAT HAPPENS WITHOUT self?
# ============================================================

class BrokenStudent:
    def __init__(self, name):
        name = name     # local variable -- disappears after __init__ ends
        courses = []    # local variable -- disappears after __init__ ends

b = BrokenStudent("Pravat")
# print(b.name)     # AttributeError: 'BrokenStudent' object has no attribute 'name'
# print(b.courses)  # AttributeError: same problem

print("\nWithout self, attributes don't exist on the object.")
print("self.name = name  PINS it to the object permanently.")

# ============================================================
# VISUALIZING self
#
#   s1 = Student("Pravat")
#
#   Memory:
#   s1 ──► [ object at 0x7f1a ]
#               .name     = "Pravat"
#               .courses  = []
#               .attendance = {}
#
#   s2 = Student("Asha")
#
#   s2 ──► [ object at 0x7f2b ]   <-- completely different place
#               .name     = "Asha"
#               .courses  = []
#               .attendance = {}
#
#   self inside __init__ just means:
#   "the object currently being set up right now"
# ============================================================





# ============================================================
# CONCEPT: Instance methods
# WHY: Methods are functions that belong to an object.
#      They can READ and MODIFY that object's own data via self.
# ============================================================

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.attendance = {}

    # --- instance method: adds a course to THIS student ---
    def enroll(self, course_name):
        if course_name not in self.courses:       # guard: no duplicates
            self.courses.append(course_name)      # modifies THIS student's list
            self.attendance[course_name] = 0      # starts attendance at 0
            print(f"{self.name} enrolled in {course_name}")
        else:
            print(f"{self.name} is already in {course_name}")

    # --- instance method: reads THIS student's data ---
    def show(self):
        print(f"\nStudent : {self.name}")
        print(f"Courses : {self.courses}")
        print(f"Attendance: {self.attendance}")


# --- Using the methods ---
s1 = Student("Pravat")
s2 = Student("Asha")

s1.enroll("Math")       # only affects s1
s1.enroll("Physics")
s1.enroll("Math")       # duplicate -- blocked by the guard

s2.enroll("English")    # only affects s2

s1.show()
s2.show()

# ============================================================
# HOW PYTHON CALLS METHODS UNDER THE HOOD
#
#   s1.enroll("Math")
#   is secretly the same as:
#   Student.enroll(s1, "Math")
#
#   Python automatically passes s1 in as self.
#   That's why self is always the first parameter --
#   you never pass it yourself, Python does.
# ============================================================

print("\n--- Proof: calling via class directly ---")
Student.enroll(s1, "Chemistry")   # same as s1.enroll("Chemistry")
s1.show()


# ============================================================
# CONCEPT: Dictionary as object store
# WHY: self.students = {} stores Student OBJECTS as values,
#      not just strings or numbers.
#      Key = student name, Value = the actual Student object.
# ============================================================

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []


# --- Normal dict: stores simple values ---
simple = {
    "Pravat": 95,      # value is a number
    "Asha"  : 88,
}
print("Simple dict value:", simple["Pravat"])       # 95
print("Type:", type(simple["Pravat"]))              # <class 'int'>

print()

# --- Object store dict: stores objects as values ---
students = {}
students["Pravat"] = Student("Pravat")   # value is a Student object
students["Asha"]   = Student("Asha")

print("Object store value:", students["Pravat"])           # <Student object>
print("Type:", type(students["Pravat"]))                   # <class '__main__.Student'>
print("Access attribute:", students["Pravat"].name)        # Pravat
print("Access attribute:", students["Pravat"].courses)     # []

print()

# --- You can call methods on the stored object directly ---
students["Pravat"].courses.append("Math")
print("After modifying:", students["Pravat"].courses)      # ['Math']

print()

# --- Iterating over all stored objects ---
for name, student_obj in students.items():
    print(f"Key: {name!r}  |  Value: Student(name={student_obj.name!r}, courses={student_obj.courses})")

# ============================================================
# MENTAL MODEL:
#
#   self.students = {
#       "Pravat" : Student object ──► .name="Pravat"  .courses=["Math"]
#       "Asha"   : Student object ──► .name="Asha"    .courses=[]
#   }
#
#   The dict is just a lookup table.
#   The actual data lives inside the Student objects.
#   The key gives you fast access to the right object.
#
#   self.students["Pravat"].courses   -- two-step access:
#       step 1: dict lookup   -> gets the Student object
#       step 2: .courses      -> gets that object's attribute
# ============================================================


# ============================================================
# CONCEPT: Instance methods
# WHY: Methods are functions that belong to an object.
#      They can READ and MODIFY that object's own data via self.
# ============================================================

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.attendance = {}

    # --- instance method: adds a course to THIS student ---
    def enroll(self, course_name):
        if course_name not in self.courses:       # guard: no duplicates
            self.courses.append(course_name)      # modifies THIS student's list
            self.attendance[course_name] = 0      # starts attendance at 0
            print(f"{self.name} enrolled in {course_name}")
        else:
            print(f"{self.name} is already in {course_name}")

    # --- instance method: reads THIS student's data ---
    def show(self):
        print(f"\nStudent : {self.name}")
        print(f"Courses : {self.courses}")
        print(f"Attendance: {self.attendance}")


# --- Using the methods ---
s1 = Student("Pravat")
s2 = Student("Asha")

s1.enroll("Math")       # only affects s1
s1.enroll("Physics")
s1.enroll("Math")       # duplicate -- blocked by the guard

s2.enroll("English")    # only affects s2

s1.show()
s2.show()

# ============================================================
# HOW PYTHON CALLS METHODS UNDER THE HOOD
#
#   s1.enroll("Math")
#   is secretly the same as:
#   Student.enroll(s1, "Math")
#
#   Python automatically passes s1 in as self.
#   That's why self is always the first parameter --
#   you never pass it yourself, Python does.
# ============================================================

print("\n--- Proof: calling via class directly ---")
Student.enroll(s1, "Chemistry")   # same as s1.enroll("Chemistry")
s1.show()

# ============================================================
# CONCEPT: Composition
# WHY: One class can OWN objects of another class.
#      Institute doesn't inherit from Student --
#      it CONTAINS Student objects inside a dictionary.
#      "has-a" relationship, not "is-a".
# ============================================================

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.attendance = {}


class Institute:
    def __init__(self):
        self.students = {}   # key = name string, value = Student object

    def add_student(self, name):
        if name not in self.students:
            self.students[name] = Student(name)   # Student object created HERE
            print(f"Added student: {name}")       # and stored inside Institute
        else:
            print(f"{name} already exists")

    def show_all(self):
        print(f"\nTotal students: {len(self.students)}")
        for name, student_obj in self.students.items():
            print(f"  {name} -> courses: {student_obj.courses}")


# --- Institute CONTAINS students, it doesn't become one ---
institute = Institute()

institute.add_student("Pravat")
institute.add_student("Asha")
institute.add_student("Pravat")   # duplicate -- blocked

institute.show_all()

# --- Accessing a student object from inside Institute ---
pravat = institute.students["Pravat"]   # get the Student object
pravat.courses.append("Math")           # now modify it directly

institute.show_all()   # change is reflected inside Institute too

# ============================================================
# COMPOSITION vs INHERITANCE
#
#   Inheritance  (is-a):   class Institute(Student)
#                          Institute IS a Student -- wrong
#
#   Composition  (has-a):  class Institute:
#                              self.students = {}  <-- HAS Students
#                          Institute HAS Students -- correct
#
#   self.students = {
#       "Pravat" : <Student object>,
#       "Asha"   : <Student object>,
#   }
#   The dictionary IS the composition -- it holds the objects.
# ============================================================

# ============================================================
# CONCEPT: Default arguments
# WHY: Let a parameter have a fallback value so the caller
#      doesn't have to pass it every time.
#      In the project: file_name="data.json"
# ============================================================

# --- Simple function example first ---
def greet(name, message="Hello"):   # message has a default
    print(f"{message}, {name}!")

greet("Pravat")              # uses default  -> Hello, Pravat!
greet("Asha", "Good morning") # overrides   -> Good morning, Asha!

print()

# --- Now in a class (exactly like the project) ---
class Institute:
    def __init__(self, file_name="data.json"):   # default file name
        self.file_name = file_name
        print(f"Institute will save to: {self.file_name}")


i1 = Institute()                    # uses default  -> data.json
i2 = Institute("backup.json")       # overrides     -> backup.json
i3 = Institute(file_name="test.json") # explicit keyword -> test.json

# ============================================================
# RULES FOR DEFAULT ARGUMENTS
#
#   def __init__(self, file_name="data.json"):
#                              ↑
#                   this value is used ONLY if caller
#                   doesn't pass anything
#
#   IMPORTANT: defaults must come AFTER non-default params
#
#   VALID:   def fn(a, b="x")       -- a required, b optional
#   INVALID: def fn(a="x", b)       -- SyntaxError
# ============================================================

print()

# --- Showing the rule violation ---
try:
    exec("def broken(a='x', b): pass")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
    print("Non-default argument 'b' follows default argument 'a' -- not allowed")


    # ============================================================
# CONCEPT: Dictionary as object store
# WHY: self.students = {} stores Student OBJECTS as values,
#      not just strings or numbers.
#      Key = student name, Value = the actual Student object.
# ============================================================

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []


# --- Normal dict: stores simple values ---
simple = {
    "Pravat": 95,      # value is a number
    "Asha"  : 88,
}
print("Simple dict value:", simple["Pravat"])       # 95
print("Type:", type(simple["Pravat"]))              # <class 'int'>

print()

# --- Object store dict: stores objects as values ---
students = {}
students["Pravat"] = Student("Pravat")   # value is a Student object
students["Asha"]   = Student("Asha")

print("Object store value:", students["Pravat"])           # <Student object>
print("Type:", type(students["Pravat"]))                   # <class '__main__.Student'>
print("Access attribute:", students["Pravat"].name)        # Pravat
print("Access attribute:", students["Pravat"].courses)     # []

print()

# --- You can call methods on the stored object directly ---
students["Pravat"].courses.append("Math")
print("After modifying:", students["Pravat"].courses)      # ['Math']

print()

# --- Iterating over all stored objects ---
for name, student_obj in students.items():
    print(f"Key: {name!r}  |  Value: Student(name={student_obj.name!r}, courses={student_obj.courses})")

# ============================================================
# MENTAL MODEL:
#
#   self.students = {
#       "Pravat" : Student object ──► .name="Pravat"  .courses=["Math"]
#       "Asha"   : Student object ──► .name="Asha"    .courses=[]
#   }
#
#   The dict is just a lookup table.
#   The actual data lives inside the Student objects.
#   The key gives you fast access to the right object.
#
#   self.students["Pravat"].courses   -- two-step access:
#       step 1: dict lookup   -> gets the Student object
#       step 2: .courses      -> gets that object's attribute
# ============================================================
