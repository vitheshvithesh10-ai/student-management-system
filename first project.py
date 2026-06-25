
students = []

def add_student():
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    department = input("Enter Department: ")

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Department": department
    }

    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\nStudent Records:")
        for student in students:
            print("---------------------")
            print("Name:", student["Name"])
            print("Roll No:", student["Roll No"])
            print("Department:", student["Department"])
        print()

def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    for student in students:
        if student["Roll No"] == roll_no:
            print("\nStudent Found:")
            print("Name:", student["Name"])
            print("Roll No:", student["Roll No"])
            print("Department:", student["Department"])
            print()
            return

    print("Student not found.\n")

while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.\n")