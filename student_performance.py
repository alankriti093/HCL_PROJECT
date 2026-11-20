# =====================================================
#       STUDENT PERFORMANCE ANALYSIS SYSTEM
#       Mini Project using Python, Pandas, NumPy
# =====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# List to store student records
students = []

subjects = ["Python", "Maths", "Physics", "Chemistry", "English"]


# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 33:
        return "E"
    else:
        return "F"


# Function to add student
def add_student():

    print("\n------ ADD STUDENT DETAILS ------")

    name = input("Enter Student Name: ")

    try:
        roll = int(input("Enter Roll Number: "))

        if any(s["Roll No"] == roll for s in students):
            print("Roll number already exists!")
            return

        marks = []

        for subject in subjects:
            while True:
                try:
                    mark = float(input(f"Enter {subject} Marks (0-100): "))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Marks must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

        marks_array = np.array(marks)

        total = np.sum(marks_array)
        average = np.mean(marks_array)
        percentage = (total / 500) * 100

        if np.min(marks_array) < 33:
            result = "Fail"
            grade = "F"
        else:
            result = "Pass"
            grade = calculate_grade(percentage)

        student = {
            "Name": name,
            "Roll No": roll,
            "Python": marks[0],
            "Maths": marks[1],
            "Physics": marks[2],
            "Chemistry": marks[3],
            "English": marks[4],
            "Total": total,
            "Average": round(average, 2),
            "Percentage": round(percentage, 2),
            "Grade": grade,
            "Result": result
        }

        students.append(student)

        print("\nStudent added successfully!")

    except ValueError:
        print("Invalid Roll Number!")


# Function to display all students
def view_students():

    print("\n------ ALL STUDENT RECORDS ------")

    if not students:
        print("No student records available.")
        return

    df = pd.DataFrame(students)

    print(df.to_string(index=False))


# Function to search student
def search_student():

    print("\n------ SEARCH STUDENT ------")

    try:
        roll = int(input("Enter Roll Number: "))

        for student in students:
            if student["Roll No"] == roll:
                print("\nStudent Found!")
                for key, value in student.items():
                    print(key, ":", value)
                return

        print("Student not found.")

    except ValueError:
        print("Enter a valid Roll Number.")


# Function to show topper
def show_topper():

    if not students:
        print("No student records available.")
        return

    df = pd.DataFrame(students)

    topper = df.loc[df["Percentage"].idxmax()]

    print("\n------ CLASS TOPPER ------")
    print("Name:", topper["Name"])
    print("Roll Number:", topper["Roll No"])
    print("Percentage:", topper["Percentage"], "%")
    print("Grade:", topper["Grade"])


# Function to show class analysis
def class_analysis():

    if not students:
        print("No student records available.")
        return

    df = pd.DataFrame(students)

    print("\n------ CLASS PERFORMANCE ANALYSIS ------")

    print("Total Students:", len(df))

    print("Class Average:",
          round(np.mean(df["Percentage"]), 2), "%")

    print("Highest Percentage:",
          df["Percentage"].max(), "%")

    print("Lowest Percentage:",
          df["Percentage"].min(), "%")

    print("Passed Students:",
          len(df[df["Result"] == "Pass"]))

    print("Failed Students:",
          len(df[df["Result"] == "Fail"]))

    print("\nSubject-wise Average Marks:")

    print(df[subjects].mean().round(2))


# Function to generate graphs
def show_graphs():

    if not students:
        print("No student records available.")
        return

    df = pd.DataFrame(students)

    # Student percentage graph
    plt.figure(figsize=(9, 5))

    plt.bar(df["Name"], df["Percentage"])

    plt.xlabel("Student Name")
    plt.ylabel("Percentage")
    plt.title("Student Performance Analysis")

    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

    # Subject-wise average graph
    plt.figure(figsize=(9, 5))

    df[subjects].mean().plot(kind="bar")

    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.title("Subject-wise Performance")

    plt.tight_layout()
    plt.show()


# Function to save records
def save_report():

    if not students:
        print("No records to save.")
        return

    df = pd.DataFrame(students)

    df.to_csv("student_performance_report.csv", index=False)

    print("\nReport saved successfully!")
    print("File: student_performance_report.csv")


# Function to load saved records
def load_report():

    global students

    if os.path.exists("student_performance_report.csv"):

        try:
            df = pd.read_csv("student_performance_report.csv")

            students = df.to_dict(orient="records")

            print("Previous student records loaded successfully!")

        except (ValueError, KeyError, pd.errors.ParserError):
            print("Could not load the saved report.")

    else:
        print("No previous report found.")


# Main menu
def main():

    load_report()

    while True:

        print("\n")
        print("==========================================")
        print("   STUDENT PERFORMANCE ANALYSIS SYSTEM")
        print("==========================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Show Class Topper")
        print("5. Class Performance Analysis")
        print("6. Show Performance Graphs")
        print("7. Save Student Report")
        print("8. Exit")

        print("==========================================")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            show_topper()

        elif choice == "5":
            class_analysis()

        elif choice == "6":
            show_graphs()

        elif choice == "7":
            save_report()

        elif choice == "8":
            save_report()
            print("\nThank you for using Student Performance Analysis System!")
            print("Program closed successfully.")
            break

        else:
            print("Invalid choice! Please select 1 to 8.")


# Starting the program
if __name__ == "__main__":
    main()

# ================= END OF PROJECT =================