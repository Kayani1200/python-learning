
students = []

while True:

    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        age = input("Enter student age: ")

        student = {
            "name": name,
            "roll_no": roll_no,
            "age": age
        }

        students.append(student)

        print("Student added successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No student records found.")

        else:
            for student in students:
                print("\nName:", student["name"])
                print("Roll Number:", student["roll_no"])
                print("Age:", student["age"])

    elif choice == "3":

        search_roll = input("Enter roll number to search: ")

        found = False

        for student in students:

            if student["roll_no"] == search_roll:
                print("Student Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                found = True

        if found == False:
            print("Student not found.")

    elif choice == "4":

        delete_roll = input("Enter roll number to delete: ")

        for student in students:

            if student["roll_no"] == delete_roll:
                students.remove(student)
                print("Student deleted successfully!")
                break

        else:
            print("Student not found.")

    elif choice == "5":

        print("Program closed.")
        break

    else:
        print("Invalid choice! Try again.")
