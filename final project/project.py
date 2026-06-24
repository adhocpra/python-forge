import json
import os

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.attendance = {}

    def enroll(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            self.attendance[course_name] = 0


class Institute:
    def __init__(self, file_name="data.json"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(base_dir, file_name)
        self.students = {}
        self.courses = []
        self.load_data()

    def save_data(self):
        data = {
            "students": {
                name: {
                    "courses": student.courses,
                    "attendance": student.attendance
                }
                for name, student in self.students.items()
            },
            "courses": self.courses
        }
        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                self.courses = data.get("courses", [])
                for name, info in data.get("students", {}).items():
                    student = Student(name)
                    student.courses = info["courses"]
                    student.attendance = info["attendance"]
                    self.students[name] = student
        except FileNotFoundError:
            self.students = {}
            self.courses = []

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"Course added successfully: {course_name}")
        else:
            print("Course already exists.")

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students[student_name] = Student(student_name)
            print(f"Student added: {student_name}")
        else:
            print("Student already exists.")

    def enroll_student(self, student_name, course_name):
        if student_name in self.students and course_name in self.courses:
            self.students[student_name].enroll(course_name)
            print(f"{student_name} enrolled in course {course_name}")
        else:
            print("Invalid course or student.")

    def mark_attendance(self, student_name, course_name):
        if student_name in self.students:
            student = self.students[student_name]
            if course_name in student.attendance:
                student.attendance[course_name] += 1
                print("Attendance marked.")
            else:
                print("Student not enrolled in course.")
        else:
            print("Student not found.")

    def show_student(self):
        if not self.students:
            print("No students registered yet.")
            return
        for name, student in self.students.items():
            print("\nName:", name)
            print("Courses:", student.courses)
            print("Attendance:", student.attendance)

    def most_popular_course(self):
        count = {}
        for student in self.students.values():
            for c in student.courses:
                count[c] = count.get(c, 0) + 1
        if count:
            popular = max(count, key=count.get)
            print("Most popular course:", popular)
        else:
            print("No data.")

    def menu(self):
        while True:
            print("\n--- Smart Institute System ---")
            print("1. Add Course")
            print("2. Add Student")
            print("3. Enroll Student")
            print("4. Mark Attendance")
            print("5. Show Students")
            print("6. Most Popular Course")
            print("7. Exit Program")
            choice = input("Enter choice (1-7): ")

            if choice == "1":
                self.add_course(input("Course name: "))
                self.save_data()
            elif choice == "2":
                self.add_student(input("Student name: "))
                self.save_data()
            elif choice == "3":
                self.enroll_student(
                    input("Student name: "),
                    input("Course name: ")
                )
                self.save_data()
            elif choice == "4":
                self.mark_attendance(
                    input("Student name: "),
                    input("Course name: ")
                )
                self.save_data()
            elif choice == "5":
                self.show_student()
            elif choice == "6":
                self.most_popular_course()
            elif choice == "7":
                print("Exiting Program...")
                break
            else:
                print("Invalid choice. Enter 1-7.")


if __name__ == "__main__":
    system = Institute()
    system.menu()
