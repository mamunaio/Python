class Student:
    def __init__(self, name, roll, gpa):
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}, GPA: {self.gpa}")

student_list = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student (Type: add)")
    print("2. View Student (Type: view)")
    print("3. Exit (Type: quit)")

    choice = input("Enter your choice: ")

    if choice == "add":
        n = input("Enter Name: ")
        r = input("Enter Roll: ")
        g = input("Enter GPA: ")

        s = Student(n, r, g)

        student_list.append(s)
        print("✅ Student added successfully!")

    elif choice == "view":
        print("\n--- Student List ---")
        # লুপ চালিয়ে দেখা
        for s in student_list:
            s.display()

    elif choice == "quit":
        print("Tata Bye Bye 👋")
        break

    else:
        print("❌ Invalid Choice! Try Again")