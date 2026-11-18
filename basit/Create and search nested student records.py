
students = {
    101: {
        "name": "Ali",
        "age": 20,
        "marks": 85
    },
    102: {
        "name": "Ahmed",
        "age": 21,
        "marks": 90
    },
    103: {
        "name": "Basit",
        "age": 22,
        "marks": 78
    }
}

print("===== STUDENT RECORDS =====")

# Display all student records
for student_id, details in students.items():
    print("\nStudent ID:", student_id)
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Marks:", details["marks"])

# Search student
search_id = int(input("\nEnter Student ID to search: "))

if search_id in students:
    print("\nStudent Found!")
    print("Name:", students[search_id]["name"])
    print("Age:", students[search_id]["age"])
    print("Marks:", students[search_id]["marks"])

else:
    print("Student Not Found!")
