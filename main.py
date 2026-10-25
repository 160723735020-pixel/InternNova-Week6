import json
import os

class Person:
def init(self, name, age):
self.name = name
self.age = age

class Student(Person):
def init(self, student_id, name, age, course, marks):
super().init(name, age)
self.__student_id = student_id
self.course = course
self.marks = marks

@property
def student_id(self):
    return self.__student_id

def calculate_grade(self):
    if self.marks >= 90:
        return "A"
    elif self.marks >= 75:
        return "B"
    elif self.marks >= 60:
        return "C"
    elif self.marks >= 40:
        return "D"
    return "F"

def display(self):
    print("\nStudent ID:", self.student_id)
    print("Name:", self.name)
    print("Age:", self.age)
    print("Course:", self.course)
    print("Marks:", self.marks)
    print("Grade:", self.calculate_grade())

class StudentManagementSystem:
def init(self):
self.students = []
self.filename = "students.json"
self.load_students()

def load_students(self):
    if os.path.exists(self.filename):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            for item in data:
                student = Student(
                    item["student_id"],
                    item["name"],
                    item["age"],
                    item["course"],
                    item["marks"]
                )
                self.students.append(student)

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Unable to load student records.")

def save_students(self):
    data = []

    for student in self.students:
        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "marks": student.marks
        })

    with open(self.filename, "w") as file:
        json.dump(data, file, indent=4)

def add_student(self):
    try:
        student_id = input("Enter student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        if any(s.student_id == student_id for s in self.students):
            print("Student ID already exists.")
            return

        name = input("Enter student name: ").strip()
        age = int(input("Enter age: "))
        course = input("Enter course: ").strip()
        marks = float(input("Enter marks (0-100): "))

        if not name or not course:
            print("Name and course cannot be empty.")
            return

        if age <= 0 or not 0 <= marks <= 100:
            print("Invalid age or marks.")
            return

        student = Student(
            student_id, name, age, course, marks
        )

        self.students.append(student)
        self.save_students()
        print("Student added successfully.")

    except ValueError:
        print("Enter valid numeric values for age and marks.")

def view_students(self):
    if not self.students:
        print("No student records found.")
        return

    for student in self.students:
        student.display()

def search_student(self):
    student_id = input("Enter student ID to search: ").strip()

    for student in self.students:
        if student.student_id == student_id:
            student.display()
            return

    print("Student not found.")

def delete_student(self):
    student_id = input("Enter student ID to delete: ").strip()

    for student in self.students:
        if student.student_id == student_id:
            self.students.remove(student)
            self.save_students()
            print("Student deleted successfully.")
            return

    print("Student not found.")

def run(self):
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            self.add_student()
        elif choice == "2":
            self.view_students()
        elif choice == "3":
            self.search_student()
        elif choice == "4":
            self.delete_student()
        elif choice == "5":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Try again.")

if name == "main":
app = StudentManagementSystem()
app.run()
