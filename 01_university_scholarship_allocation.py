# Assignment 1: University Scholarship Allocation

students = []
count = int(input("Enter number of students: "))

for i in range(count):
    print(f"\nStudent {i + 1}")
    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate percentage: "))
    attendance = float(input("Enter attendance percentage: "))
    family_income = float(input("Enter annual family income (Rs.): "))

    print("Enter marks in 3 subjects:")
    marks = []
    for j in range(3):
        marks.append(float(input(f"Subject {j + 1}: ")))

    eligible = (
        aggregate >= 80
        and attendance >= 75
        and family_income <= 250000
        and min(marks) >= 60
    )

    students.append({
        "name": name,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": family_income,
        "eligible": eligible
    })

eligible_students = [student for student in students if student["eligible"]]
eligible_students.sort(
    key=lambda student: (student["aggregate"], student["attendance"]),
    reverse=True
)

print("\n--- Scholarship Results ---")
if not eligible_students:
    print("No students are eligible for the scholarship.")
else:
    for rank, student in enumerate(eligible_students, start=1):
        print(
            f"Rank {rank}: {student['name']} | "
            f"Aggregate: {student['aggregate']:.2f}% | "
            f"Attendance: {student['attendance']:.2f}%"
        )

print(f"\nEligible students: {len(eligible_students)} out of {count}")
