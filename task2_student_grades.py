# Task 2: Student Grades
student_grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        name = input("Enter new student's name: ")
        if name in student_grades:
            print(f"{name} already exists with grade {student_grades[name]}.")
        else:
            grade = input(f"Enter grade for {name}: ").upper()
            student_grades[name] = grade
            print(f"Added {name} with grade {grade}.")
            
    elif choice == "2":
        name = input("Enter student's name to update: ")
        if name in student_grades:
            grade = input(f"Enter new grade for {name}: ").upper()
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
        else:
            print(f"Student '{name}' not found.")
            
    elif choice == "3":
        print("\nAll Student Grades:")
        for student, grade in student_grades.items():
            print(f"- {student}: {grade}")
            
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
