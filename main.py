#1st think all types of data that we need to store
#specefic user list

#dictionary



student_grades = {}

def add_grades(name, grades):
    if name in student_grades:
        print(f"Student {name} already exists. Use update option to modify grades.")
    else:
        student_grades[name] = grades
        print(f"Grades for {name} added successfully.")


def update_grades(name, grades):
    if name in student_grades:
        student_grades[name] = grades
        print(f"Grades for {name} updated successfully.")
    else:
        print(f"Student {name} does not exist. Use add option to add new student.")


def view_grades(name):
    if name in student_grades:
        print(f"Grades for {name}: {student_grades[name]}")
    else:
        print(f"Student {name} does not exist.")


def student_average(name):
    if name in student_grades:
        average = sum(student_grades[name]) / len(student_grades[name])
        print(f"Average grade for {name}: {average:.2f}")
    else:
        print(f"Student {name} does not exist.")


def class_average():
    if student_grades:
        total_grades = [grade for grades in student_grades.values() for grade in grades]
        average = sum(total_grades) / len(total_grades)
        print(f"Class average grade: {average:.2f}")
    else:
        print("No students in the class.")



def parse_grades(grades_str):
    grades = []
    for grade in grades_str.split():
        try:
            grades.append(int(grade))
        except ValueError:
            print(f"Invalid grade '{grade}' input. Please enter numeric values separated by spaces.")
            return []
    return grades





def main():
    while True:
        print("\n1. Add a new student's grades")
        print("2. Update an existing student's grades")
        print("3. View a student's grades")
        print("4. Calculate and display the average grade of a student")
        print("5. Calculate and display the class average grade")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            grades_str = input("Enter grades separated by space: ")
            grades = parse_grades(grades_str)
            if grades:
                add_grades(name, grades)
        elif choice == '2':
            name = input("Enter student name to update: ")
            grades_str = input("Enter new grades separated by space: ")
            grades = parse_grades(grades_str)
            if grades:
                update_grades(name, grades)
        elif choice == '3':
            name = input("Enter student name: ")
            view_grades(name)
        elif choice == '4':
            name = input("Enter student name: ")
            student_average(name)
        elif choice == '5':
            class_average()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()            
