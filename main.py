from db_utils import create_table
from student import add_student, view_students, update_student, delete_student

create_table()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        add_student(name, age, course)

    elif choice == "2":
        view_students()

    elif choice == "3":
        sid = int(input("ID: "))
        name = input("New Name: ")
        age = int(input("New Age: "))
        course = input("New Course: ")
        update_student(sid, name, age, course)

    elif choice == "4":
        sid = int(input("ID: "))
        delete_student(sid)

    elif choice == "5":
        break

    else:
        print("Invalid choice")