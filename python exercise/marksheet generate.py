def generate_marksheet(student_details, subjects):
    print("\nMarksheet:")
    print(f"Name: {student_details[0]}")
    print(f"Roll Number: {student_details[1]}")
    print("Subject-wise Marks:")

    total_marks = 0
    for subject in subjects:
        print(f"{subject[0]}: {subject[1]}")
        total_marks += subject[1]

    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {total_marks / len(subjects):.2f}%")


student_details = ("John Doe", "12345")

subjects = [
    ("Math", 95),
    ("English", 88),
    ("Science", 92),
    ("History", 85),
    ("Geography", 90)
]

generate_marksheet(student_details, subjects)