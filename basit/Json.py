
import json
import os

FILE_NAME = "students.json"


# Load student records from JSON
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save student records in JSON
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)


# Add a new student
def add_student(students):
    student_id = input("Enter Student ID: ")

    if any(s["id"] == student_id for s in students):
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")

    marks = []
    for i in range(3):
        mark = float(input(f"Enter Subject {i+1} Marks: "))

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100!")
            return

        marks.append(mark)

    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# Search student
def search_student(students):
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("Student Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Average:", calculate_average(student["marks"]))
            return

    print("Student not found!")


# Update student
def update_student(students):
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:

            student["name"] = input("Enter New Name: ")

            marks = []
            for i in range(3):
                mark = float(input(f"Enter New Subject {i+1} Marks: "))

                if mark < 0 or mark > 100:
                    print("Invalid marks!")
                    return

                marks.append(mark)

            student["marks"] = marks
            save_students(students)

            print("Student updated successfully!")
            return

    print("Student not found!")


# Delete student
def delete_student(students):
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found!")


# Show all students and averages
def show_students(students):
    if not students:
        print("No student records found!")
        return

    for student in students:
        average = calculate_average(student["marks"])

        print("\nID:", student["id"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Average:", round(average, 2))


# Show top 3 students
def top_students(students):
    if not students:
        print("No student records found!")
        return

    sorted_students = sorted(
        students,
        key=lambda s: calculate_average(s["marks"]),
        reverse=True
    )

    print("\nTop Students:")

    for student in sorted_students[:3]:
        average = calculate_average(student["marks"])

        print(
            student["name"],
            "- Average:",
            round(average, 2)
        )


# Main program
students = load_students()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Show All Students")
    print("6. Calculate Average Marks")
    print("7. Show Top Students")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        update_student(students)

    elif choice == "3":
        delete_student(students)

    elif choice == "4":
        search_student(students)

    elif choice == "5":
        show_students(students)

    elif choice == "6":
        show_students(students)

    elif choice == "7":
        top_students(students)

    elif choice == "8":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
