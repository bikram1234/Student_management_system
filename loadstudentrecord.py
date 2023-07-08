import csv
import os

# define a function to add a new student record to the list of students
def add_student(students):
    # prompt user for student details
    student_number = input("Enter student number: ")
    surname = input("Enter surname: ")
    given_name = input("Enter given name: ")
    unit_mark = float(input("Enter unit mark: "))
    # create a dictionary to store the student details
    student = {
        'student_number': student_number,
        'surname': surname,
        'given_name': given_name,
        'unit_mark': unit_mark
    }
    # append the new student record to the list of students
    students.append(student)
    print("Student details added successfully.")

# define a function to search for student records in the list of students
def search_students(students):
    # prompt user for search term
    search_key = input("Enter student number or name to search: ").lower()
    matching_students = []
    # loop through each student record in the list
    for student in students:
        # check if the search term matches the student's ID or name (case insensitive)
        if (search_key in student['student_number'].lower()) or (search_key in student['surname'].lower()) or (search_key in student['given_name'].lower()):
            # add the matching student record to the list of matching students
            matching_students.append(student)
    # if any matching students were found, display their details
    if len(matching_students) > 0:
        print("Matching students found:")
        for student in matching_students:
            print_student_details(student)
    else:
        print("No matching students found.")

# define a function to print the details of a single student record
def print_student_details(student):
    print("Student Number:", student['student_number'])
    print("Surname:", student['surname'])
    print("Given Name:", student['given_name'])
    print("Unit Mark:", student['unit_mark'])
    print()

# define a function to display all student records with a given grade
def display_students_by_grade(students):
    # prompt user for the grade to filter by
    grade = input("Enter unit grade (HD, D, C, P, or N): ")
    grade_students = []
    # loop through each student record in the list
    for student in students:
        # convert the student's mark to a grade and check if it matches the requested grade
        student_grade = convert_mark_to_grade(student['unit_mark'])
        if student_grade == grade:
            # add the matching student record to the list of grade students
            grade_students.append(student)
    # if any grade students were found, display their details
    if len(grade_students) > 0:
        print("Students with grade", grade + ":")
        for student in grade_students:
            print_student_details(student)
    else:
        print("No students found with grade", grade + ".")

# define a function to convert a numeric mark to a letter grade
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

# define a function to delete a student record from the list of students
def delete_student(students):
    # prompt user for the student ID to delete
    student_number = input("Enter student number to delete: ")
    deleted = False
    # loop through each student record in the list
    for student in students:
        # check if the current student's ID matches the ID to delete
        if student['student_number'] == student_number:
            # remove the matching student record from the list of students
            students.remove(student)
            deleted = True
            break
    # print a success or error message based on whether the student was found and deleted
    if deleted:
        print("Student", student_number, "deleted successfully.")
    else:
        print("Student", student_number, "not found.")

# define a function to load student records from a CSV file into the list of students
def load_students_from_file(students):
    # prompt user for the path to the CSV file to load
    file_path = input("Enter path to CSV file: ")
    # check if the file exists
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return
    # open the CSV file and loop through each row (skipping the header row)
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for row in reader:
            try:
                # extract the student details from the current row and add them to the list of students
                student_number = row[0]
                surname = row[1]
                given_name = row[2]
                unit_mark = float(row[3])
                student = {
                    'student_number': student_number,
                    'surname': surname,
                    'given_name': given_name,
                    'unit_mark': unit_mark
                }
                students.append(student)
            except ValueError:
                # if there was an error parsing the mark as a float, skip this row and print an error message
                print("Error loading row:", row)
        # print the number of students that were loaded from the file
        print(len(students), "students loaded from file", file_path)

# define a function to save the list of students to a CSV file
def save_students_to_file(students):
    # prompt user for the path to the CSV file to save
    file_path = input("Enter path to save CSV file: ")
    # check if the file already exists and prompt the user before overwriting it
    if os.path.exists(file_path):
        choice = input(f"{file_path} already exists. Do you want to overwrite it? (y/n)")
        if choice != 'y':
            print("Operation cancelled. No changes were made.")
            return
    # open the CSV file for writing, write the header row, then loop through each student record and write it to the file
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['student_number', 'surname', 'given_name', 'unit_mark']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
        # print the number of students that were saved to the file
        print(len(students), "students saved to file", file_path)

# define a function to print the program menu
def print_menu():
    print("Menu:")
    print("1. Add student details")
    print("2. Search for students")
    print("3. Display students by grade")
    print("4. Delete student record")
    print("5. Load student records from a CSV file")
    print("6. Save the student records in the current system to a CSV file")
    print("7. Quit")

# define the main function that runs the program
def main():
    students = []

    # load initial student records from file
    load_students_from_file(students)

    # loop until the user chooses to quit
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            search_students(students)
        elif choice == '3':
            display_students_by_grade(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            load_students_from_file(students)
        elif choice == '6':
            save_students_to_file(students)
        elif choice == '7':
            print("Quitting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

# execute the main function if this script is run as the main module
if __name__ == '__main__':
    main()
