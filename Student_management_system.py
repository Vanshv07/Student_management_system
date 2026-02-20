# pylint: disable=missing-module-docstring, missing-function-docstring

students = []

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students.append({"roll": roll, "name": name, "marks": marks})
    print("Student added successfully.")

def display_students():
    if not students:
        print("No student records found.")
        return
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")

def search_student():
    roll = int(input("Enter Roll Number to Search: "))
    for s in students:
        if s["roll"] == roll:
            print(s)
            return
    print("Student not found.")

def update_marks():
    roll = int(input("Enter Roll Number to Update Marks: "))
    for s in students:
        if s["roll"] == roll:
            s["marks"] = float(input("Enter New Marks: "))
            print("Marks updated successfully.")
            return
    print("Student not found.")

def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student record deleted.")
            return
    print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Exiting Program.")
        break
    else:
        print("Invalid choice.")
