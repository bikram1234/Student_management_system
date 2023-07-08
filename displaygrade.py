import csv
import os
import numpy as np
import matplotlib.pyplot as plt

# Function for adding a new student to the records
def add_student(students):
    # Prompt user for input data
    student_number = input("Enter student number: ")
    surname = input("Enter surname: ")
    given_name = input("Enter given name: ")
    unit_mark = float(input("Enter unit mark: "))
    
    # Create dictionary of student data and append it to the array of students
    student = {
        'student_number': student_number,
        'surname': surname,
        'given_name': given_name,
        'unit_mark': unit_mark
    }
    students = np.append(students, student)
    
    # Print success message and return updated array of students
    print("Student details added successfully.")
    return students

# Function for searching the records for students based on a keyword
def search_students(students):
    # Prompt user for search keyword
    search_key = input("Enter student number or name to search: ").lower()
    matching_students = []
    
    # Check each student in the array for a match with the search key
    for student in students:
        if (search_key in student['student_number'].lower()) or (search_key in student['surname'].lower()) or (search_key in student['given_name'].lower()):
            matching_students.append(student)
    
    # Print list of matching students if any found, else print error message
    if len(matching_students) > 0:
        print("Matching students found:")
        for student in matching_students:
            print_student_details(student)
    else:
        print("No matching students found.")

# Helper function for printing details of a single student record
def print_student_details(student):
    print("Student Number:", student['student_number'])
    print("Surname:", student['surname'])
    print("Given Name:", student['given_name'])
    print("Unit Mark:", student['unit_mark'])
    print()

# Function for displaying all students in a particular grade range
def display_students_by_grade(students):
    # Prompt user for target grade
    grade = input("Enter unit grade (HD, D, C, P, or N): ")
    grade_students = []
    
    # Check each student in the array for a match with the target grade
    for student in students:
        student_grade = convert_mark_to_grade(student['unit_mark'])
        if student_grade == grade:
            grade_students.append(student)
    
    # Print list of matching students if any found, else print error message
    if len(grade_students) > 0:
        print("Students with grade", grade + ":")
        for student in grade_students:
            print_student_details(student)
    else:
        print("No students found with grade", grade + ".")

# Helper function for converting a numeric mark to a letter grade
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

# Function for deleting a student record from the array
def delete_student(students):
    # Prompt user for target student number
    student_number = input("Enter student number to delete: ")
    deleted = False
    
    # Check each student in the array for a match with the target student number
    for index, student in enumerate(students):
        if student['student_number'] == student_number:
            students = np.delete(students, index)
            deleted = True
            break
    
    # Print success message or error message if no matching student found
    if deleted:
        print("Student", student_number, "deleted successfully.")
    else:
        print("Student", student_number, "not found.")
    
    # Return updated array of students
    return students

# Function for loading student records from a CSV file and adding them to the existing array
def load_students_from_file(students):
    # Prompt user for file path and check if file exists
    file_path = input("Enter path to CSV file: ")
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return students
    
    # Open file and read each row as a new student, then add to the array
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for row in reader:
            try:
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
                students = np.append(students, student)
            except ValueError:
                print("Error loading row:", row)
        
        # Print success message and return updated array of students
        print(len(students), "students loaded from file", file_path)
    return students

# Function for saving all current student records to a CSV file
def save_students_to_file(students):
    # Prompt user for file path and check if file exists, giving option to overwrite if it does
    file_path = input("Enter path to save CSV file: ")
    if os.path.exists(file_path):
        choice = input(f"{file_path} already exists. Do you want to overwrite it? (y/n)")
        if choice != 'y':
            print("Operation cancelled. No changes were made.")
            return
    
    # Open file and write header row, then write each student record as a new row
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['student_number', 'surname', 'given_name', 'unit_mark']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
        print(len(students), "students saved to file", file_path)

# Function for displaying a pie chart showing the distribution of grades among all students
def display_grade_distribution(students):
    grades, counts = np.unique([convert_mark_to_grade(student['unit_mark']) for student in students], return_counts=True)
    plt.pie(counts, labels=grades)
    plt.title('Grade Distribution')
    plt.show()

# Function for displaying a bar chart showing the distribution of numeric marks among all students
def display_marks_distribution(students):
    marks = [student['unit_mark'] for student in students]
    bins = [0, 30, 40, 50, 60, 70, 80, 90, 100]
    categories = ['0-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-100']
    hist, _ = np.histogram(marks, bins=bins)
    percent = hist/len(marks) * 100
    plt.bar(categories, percent)
    plt.title('Marks Distribution')
    plt.xlabel('Mark Ranges')
    plt.ylabel('Percentage')
    plt.show()

# Function for printing the main menu of options and prompting user for choice
def print_menu():
    print("Menu:")
    print("1. Add student details")
    print("2. Search for students")
    print("3. Display students by grade")
    print("4. Delete student record")
    print("5. Load student records from a CSV file")
    print("6. Save the student records in the current system to a CSV file")
    print("7. Quit")
    print("8. Display grade distribution")
    print("9. Display marks distribution")

# Main function that controls program flow
def main():
    students = np.array([])

    # Load initial student records from file
    students = load_students_from_file(students)

    # Display main menu and prompt user for choice until they choose to quit
    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ")
        if choice == '1':  # Call add_student() function if user chooses option 1
            students = add_student(students)
        elif choice == '2':  # Call search_students() function if user chooses option 2
            search_students(students)
        elif choice == '3':  # Call display_students_by_grade() function if user chooses option 3
            display_students_by_grade(students)
        elif choice == '4':  # Call delete_student() function if user chooses option 4
            students = delete_student(students)
        elif choice == '5':  # Call load_students_from_file() function if user chooses option 5
            students = load_students_from_file(students)
        elif choice == '6':  # Call save_students_to_file() function if user chooses option 6
            save_students_to_file(students)
        elif choice == '7':  # End program if user chooses option 7
            print("Quitting the program...")
            break
        elif choice == '8':  # Call display_grade_distribution() function if user chooses option 8
            display_grade_distribution(students)
        elif choice == '9':  # Call display_marks_distribution() function if user chooses option 9
            display_marks_distribution(students)
        else:
            # Print error message and re-prompt user for menu choice if they entered an invalid option
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main() 
