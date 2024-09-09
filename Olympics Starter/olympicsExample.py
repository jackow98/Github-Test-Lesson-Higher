# Parallel arrays representing students' names, ages, and grades
student_names = ["Leila", "Phoebe", "Rebecca"]
student_ages = [16, 15, 17]
student_grades = ["A", "B", "A"]

# A function to print details of a student from parallel arrays
def print_student_info(index):
    print("Student Name:", student_names[index])
    print("Student Age:", student_age[index])  
    print("Student Grade:", student_grades[index])
    print()  # Just adding an extra line for readability

# A function to print information for all students
def print_all_students():
    for i in range(len(student_names) + 1): 
        print_student_info(i)


