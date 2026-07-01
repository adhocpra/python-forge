#student management system
#review of lists, dict, loops, functions and conditionalsssss

#empty list to began with
students = []

#add students
def add_student():
    student={}
    student['id']=input("Enter student ID: ")
    student['name']= input("Enter student name:")
    student['age']=input("Enter student age:")
    student['grade']=input("Enter student grade:")
    students.append(student)
    print("Student added succesfully!\n")

#view students
def view_students():
    if not students: #if the list is empty
        print("No student found.\n")
        return
    print("\nList of students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade; {student['grade']}")
    print()

#search student by id or name
def search_student():
    query= input("Enter student ID or Name to search: ")
    found= False 
    for student in students:
        if student['id']== query or student['name'].lower()== query.lower():
            print(f" Found: ID : {student['id']}, Name :{student['name']},Age: {student['age']}, Grade; {student['grade']}")
            found= True
    if not found:
        print("Student not found.\n")
# update student details
def update_student():
    query= input ("Enter student ID to update :")
    for student in students:
        if student['id'] ==query:
            student['name']= input("Enter new name:")
            student['age']= input("Enter new age:")
            student['grade']= input("Enter new grade:")
            print("Students details updated succesfullt\n")
            return
    print("Student not found\n")

#delete student
def delete_student():
    query=input("Enter student ID to delete:")
    for student in students:
        if student['id']==query:
            students.remove(student)
            print("Student deleted successfully.\n")
            return
    print("Student not found. \n")

#total no of students 
def total_students():
    print(f"Total students: {len(students)}\n")

#Main menu
def main_menu():
    while True:
        print("======== Student not so mananged system.==========")
        print("1. Add student")
        print("2. View all students")
        print("3. search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Total students")
        print("7. Exit")
        choice=input("Enter your choice(1-7): ")
        
        if choice =="1":
            add_student()
        elif choice== "2":
            view_students()
        elif choice== "3":
            search_student()
        elif choice== "4":
            update_student()
        elif choice== "5":
            delete_student()
        elif choice== "6":
            total_students()
        elif choice== "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again\n")
#Run
main_menu()