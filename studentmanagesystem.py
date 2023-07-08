# Define a function to add a student to the list of students
def add_student(students):
    # Get input from user for student details
    student_number = input("Enter student number: ")
    surname = input("Enter surname: ")
    given_name = input("Enter given name: ")
    unit_mark = float(input("Enter unit mark: "))
    
    # Create a dictionary for the new student
    student = {
        'student_number': student_number,
        'surname': surname,
        'given_name': given_name,
        'unit_mark': unit_mark
    }
    
    # Append the new student to the list of students
    students.append(student)
    
    # Let the user know the student was added successfully
    print("Student details added successfully.")

# Define a function to search for a student by name or student number
def search_students(students):
    # Get input from user for search key
    search_key = input("Enter student number or name to search: ").lower()
    
    # Create an empty list to hold matching students
    matching_students = []
    
    # Loop through the list of students and append any matches to the matching_students list
    for student in students:
        if (search_key in student['student_number'].lower()) or (search_key in student['surname'].lower()) or (search_key in student['given_name'].lower()):
            matching_students.append(student)
    
    # Print the list of matching students
    if len(matching_students) > 0:
        print("Matching students found:")
        for student in matching_students:
            print_student_details(student)
    else:
        print("No matching students found.")

# Define a function to print the details of a specific student
def print_student_details(student):
    print("Student Number:", student['student_number'])
    print("Surname:", student['surname'])
    print("Given Name:", student['given_name'])
    print("Unit Mark:", student['unit_mark'])
    print()

# Define a function to display all students with a certain grade
def display_students_by_grade(students):
    # Get input from user for grade
    grade = input("Enter unit grade (HD, D, C, P, or N): ")
    
    # Create an empty list to hold students with the given grade
    grade_students = []
    
    # Loop through the list of students and append any matches to the grade_students list
    for student in students:
        student_grade = convert_mark_to_grade(student['unit_mark'])
        if student_grade == grade:
            grade_students.append(student)
    
    # Print the list of students with the given grade
    if len(grade_students) > 0:
        print("Students with grade", grade + ":")
        for student in grade_students:
            print_student_details(student)
    else:
        print("No students found with grade", grade + ".")

# Define a function to convert a numeric unit mark into a grade (HD, D, C, P, or N)
def convert_mark_to_grade(mark):
    if mark >= 85:
        return "HD"
    elif mark >= 75:
        return "D"
    elif mark >= 65:
        return "C"
    elif mark >= 50:
        return "P"
    else:
        return "N"

# Define a function to delete a student from the list of students
def delete_student(students):
    # Get input from user for student number to delete
    student_number = input("Enter student number to delete: ")
    
    # Flag variable to indicate whether student was successfully deleted
    deleted = False
    
    # Loop through the list of students and remove the one with the given student number
    for student in students:
        if student['student_number'] == student_number:
            students.remove(student)
            deleted = True
            break
    
    # Let the user know whether the student was deleted successfully or not
    if deleted:
        print("Student", student_number, "deleted successfully.")
    else:
        print("Student", student_number, "not found.")

# Define a function to print out the menu of options for the user
def print_menu():
    print("Menu:")
    print("1. Add student details")
    print("2. Search for students")
    print("3. Display students by grade")
    print("4. Delete student record")
    print("5. Quit")

# Define the main function that runs the program
def main():
    # Create an empty list of students
    students = []
    
    # Loop through the program until the user chooses to quit
    while True:
        # Print the menu of options for the user
        print_menu()
        
        # Get input from the user for their choice
        choice = input("Enter your choice (1-5): ")
        
        # Respond to the user's choice by calling the appropriate function
        if choice == '1':
            add_student(students)
        elif choice == '2':
            search_students(students)
        elif choice == '3':
            display_students_by_grade(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("Quitting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function when this file is executed
if __name__ == '__main__':
    main()
