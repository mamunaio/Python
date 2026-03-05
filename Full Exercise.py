# # for i in range(1, 6):
# #   print(i)

# for i in range(10):
#   print(i)
# for i in range(2, 11, 2):
#   print(i)
# for i in range(1, 11):
#   if i % 2 == 0:
#     print(i, "is Even")
# for i in range(1, 11):
#   print(i)
# for i in range(1, 21):
#   if i % 2 != 0:
#     print(i, "is Odd")
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#   print(num, "*", i, "=", num * i)
i = 1

# while i <= 5:
#     print(i)
#     i += 1
# i = 1

# while i <= 10:
#     if i % 2 == 0:
#         print(i, "Even")
#     i += 1
# password = ""

# while password != "1234":
#     password = input("Enter password: ")

# print("Access granted")
# এটা করবেন না
# i = 1
# while i <= 5:
#     print(i)
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# i = 1

# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# while True:
#     num = int(input("Enter a number: "))
#     if num == 0:
#         print("Program stopped")
#         break
# items = ["rice", "dal", "oil"]
# numbers = [10, 20, 30, 40]
# names = ["Mamun", "Sabbir", "Rifat", "Siam"]
# mixed = [1, "Hello", True, 3.5]
# names = ["Mamun", "Sabbir", "Rifat", "Siam"]
# print(names[0])
# print(names[1])
# print(names[2])
# for name in names:
#   print(name)
# names.append("Hasan")
# print(names)
# names[1] = "Rifat"
# print(names)
# number = [5, 10, 15, 20]
# print(len(number))
# number[1] = 100
# print(number)
# number.append(25)
# print(number)
# list = ["Python", "Django", "PHP"]
# for i in list:
#   print(i)
# numbers = [10, 15, 20, 25, 30]
# if i % 2 == 0:
#   print(i, "is Even")
# numbers = [10, 20,30]
# numbers.append(40)
# print(numbers)

# numbers.insert(1, 15)
# print(numbers)

# numbers.remove(20)
# print(numbers)

# numbers.pop()
# print(numbers)

# x = numbers.pop()
# print(x)

# numbers.clear()
# print(numbers)

# numbers = [5, 1, 4, 2]
# numbers.sort()
# print(numbers)

# numbers = [10, 20, 10, 10]
# print(numbers.count(10))

# numbers = [10, 20, 30]
# print(numbers.index(20))

# numbers = [1, 2, 3]

# numbers.append(4)
# numbers.insert(1, 10)

# print(numbers)

# numbers = [10, 20, 30, 40]

# numbers.remove(20)
# numbers.pop()
# print(numbers)

# numbers = [5, 1, 4, 2, 3]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# def greet(name):
#     print("Hello", name)

# greet("Mamun")

# def add(a, b):
#     return a + b

# print(add(5, 10))

# def add(a, b):
#     return a + b
# result = add(10, 20)
# print(result)

# def say_hello():
#     print("Hello Python")

# say_hello()

# def square(number):
#     return number * number

# print(square(5))

# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# result = check_even_odd(10)
# print(result)

# def say_hello():
#     print("Hello Python")

# say_hello()
# say_hello()
# say_hello()

# def janina(name, age):
#     print(f"What is {name} and why its {age}?")

# janina(name="Mamun", age=20)
# janina(name="Sabbir", age=21)
# janina(name="Rifat", age=22)

# def greet(name):
#     print(f"Hello {name}")

# greet("Mamun")
# greet("Sabbir")
# greet("Rifat")

# def add(a, b):
#     return a + b

# x = add(5, 10)
# print(x)

# def calculate_total(price, quantity):
#     total = price * quantity
#     return total

# bill = calculate_total(100, 3)
# print("Total bill is", bill)

# def add_numbers(a, b):
#     return a + b
# print(add_numbers(5, 10))

# def is_adult(age):
#     if age >= 18:
#         return True
#     else:
#         return False

# print(is_adult(20))

# def show_result(score):
#     if score >= 40:
#         return "Pass"
#     else:
#         return "Fail"

# print(show_result(40))

# def add_numbers(a, b):
#     return a + b
# print(add_numbers(10, 20))

# def is_adult(age):
#     return age >= 18
# print(is_adult(20))

# def show_result(score):
#     if score >= 40:
#         return "Pass"
#     else:
#         return "Fail"
# print(show_result(40))

# # প্রথম Parent Class
# class Father:
#     def hard_work(self):
#         print("Father is very hard working")

# # দ্বিতীয় Parent Class
# class Mother:
#     def love(self):
#         print("Mother is very loving")

# # Child Class
# class Child(Father, Mother):
#     def study(self):
#         print("Child is studying")

# # Child Class Object
# child = Child()
# child.hard_work()
# child.love()
# child.study()

# # Multiple Inheritance
# class GrandFather:
#     def land(self):
#         print("GrandFather has land")

# class Father(GrandFather):
#     def hard_work(self):
#         print("Father is very hard working")

# class Mother:
#     def love(self):
#         print("Mother is very loving")

# class Child(Father, Mother):
#     def study(self):
#         print("Child is studying")

# # Child Class Object
# child = Child()
# child.land()
# child.hard_work()
# child.love()
# child.study()

# class Animal:
#     def speak(self):
#         print("প্রাণী আওয়াজ করে।")

# class Dog(Animal):

#     def speak(self):
#         print("")

# class Cat(Animal):
#     # 
#     def speak(self):
#         print("")

# # অবজেক্ট তৈরি
# animal = Animal()
# dog = Dog()
# cat = Cat()

# animal.speak()
# dog.speak()
# cat.speak()

# A Simple dictionary representing a student
# student_info = {
#     "name" : "Mamun Hossain",
#     "age" : 27,
#     "team" : "Bangladesh",
#     "is_active" : True
# }

# print(student_info)
# print(student_info["is_active"])

# student_info = {
#     "name" : "Mamun",
#     "Occupation" : "Freelancer",
#     "role" : "Junior Python Developer"
# }
# print(student_info)
# print(student_info["Occupation"])
# student_info = {
#     "name": "Mamun",
#     "jersey_no": 75,
#     "role": "All-rounder"
# }

# # Accessing values using keys
# print(student_info["name"])       # Output: Mamun
# print(student_info["jersey_no"])  # Output: 75
# my_phone = {
#     "brand" : "Xiaomi",
#     "model" : "Redmi Note 12 Pro 5G",
# }

# # 1. Updating the existing value
# my_phone["model"] = "Note 15 Pro Max"

# # 2. Adding a new key-value pair
# my_phone["color"] = "Black"
# print(my_phone)

# car = { 
#     "brand" : "Toyota",
#     "model" : "Corolla",
#     "year" : 2020
# }

# # Removing 'Year'
# car.pop("year")
# print(car)

# product = {
#     "name" : "Mobile",
#     "price" : 20000,
#     "in_stock" : True
# }
# print(product["name"])

# student = {
#     "name": "Rahim",
#     "roll": 101,
#     "city": "Dhaka"
# }

# print(student.keys())
# print(student.values())
# print(student.items())

# student = {
#     "name" : "Rahim",
#     "roll" : 101,
#     "city" : "Dhaka"
# }

# K = key, V = value 
# .items use kore amra ek sathe duita variable pai

# for k, v in student.items():
#     print(f"Key is {k} and Value is {v}")

# student = { 
#     "name" : "Sakib",
#     "roll" : 102,
#     "city" : "Dhaka"
# }

# for k, v in student.items():
#     print(f"Key is {k} and Value is {v}")

# cricketer = {
#     "name" : "Mamun",
#     "runs" : 100,
#     "wickets" : 2
# }

# for k, v in cricketer.items():
#     print(f"{k}:{v}")

# players = [
#     {"name" : "Mamun", "runs" : 100, "wickets" : 2},
#     {"name" : "Sabbir", "runs" : 150, "wickets" : 1},
#     {"name" : "Rifat", "runs" : 200, "wickets" : 3}
# ]

# for p in players:
#     print(f"{p['name']} has scored {p['runs']} runs and took {p['wickets']} wickets")

# students = [
#     {"id" : 1, "marks" : 80},
#     {"id" : 2, "marks" : 90},
#     {"id" : 3, "marks" : 70}
# ]

# print(students[1]["marks"])

# Nested Loops
# for i in range(3):
#    print(f"Outer Loop i: {i} Starting ---")

#    for j in range(2):
#       print(f"-> Inner Loop j: {j} Running")

#    print(f"Outer Loop i: {i} Ending ---\n")

# 1 to 5 loop (6 will not counted)
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# try: 
#     result = 10 / 0
#     print(result)
# except:
#     print("Something went wrong")
# print("Program continues")


# try:
#     passed = 33
#     if passed >= 40:
#         print("Pass")
#     else:
#         print("Fail")
# except:
#     print("Something went wrong")3


# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except NameError:
#     print("Variable is not defined")
# except:
#     print("Something went wrong")

# try:
#     user_input = input("Enter a number: ")
#     number = int(user_input)
#     print(number)
# except ValueError:
#     print(f"Please enter a valid number")

# try:
#     print(10 / 2)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("This will always run")

# f = open("my_bio.txt", "a")
# f.write("\n I am a good boy.")
# f.close()
# print("File created successfully")

# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#     def display_info(self):
#         print(f"Student Name: {self.name}, Roll: {self.roll}")
#
# s1 = Student("Rahim", 101)
# s2 = Student("Karim", 102)
# s1.display_info()
# s2.display_info()

# class Car:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def start_engine(self):
#         print(f"{self.name} has started the engine... Vroom Vroom!")
# my_car = Car("Toyota", "5000000")
# my_car.start_engine()

# class BankAccount:
#     def __init__(self, name):
#         self.name = name
#         self.balance = 0
#         print(f"Account Created for {self.name}")
#
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print(f"{amount} Taka deposited. Current Balance {self.balance}")
#
#     def withdraw(self, amount):
#         pass
#
# my_account = BankAccount("Mamun")
# my_account.deposit(500)
# my_account.withdraw(200)

# class BankAccount:
#     def __init__(self, name):
#         self.name = name
#         self.balance = 0  # শুরুতে একাউন্টে ০ টাকা
#         print(f"Account Created for {self.name}")
#
#     def deposit(self, amount):
#         self.balance = self.balance + amount  # টাকা বাড়ছে
#         print(f"{amount} Taka deposited. Current Balance: {self.balance}")
#
#     def withdraw(self, amount):
#         # টাকা তোলার লজিক (বিয়োগ হবে)
#         self.balance = self.balance - amount
#         print(f"{amount} Taka withdrawn. Current Balance: {self.balance}")
#
# # টেস্টিং
# my_account = BankAccount("Mamun")
# my_account.deposit(500)  # ৫০০ টাকা জমা
# my_account.withdraw(200) # ২০০ টাকা তোলা

# class BankAccount:
#     def __init__(self, name):
#         self.name = name
#         self.balance = 0
#         print(f"Account Created for {self.name}")
#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         print(f"{amount} Taka withdrawn. Current Balance: {self.balance}")
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print(f"{amount} Taka deposited. Current Balance: {self.balance}")
#
# my_account = BankAccount("Mamun")
# my_account.deposit(500)
# my_account.withdraw(200)
#
# class BankAccount:
#     def __init__(self, name):
#         self.name = name
#         self.balance = 0  # শুরুতে ০ টাকা
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. Current Balance: {self.balance}")
#
#     def withdraw(self, amount):
#         # আগে চেক করছি ব্যালেন্স আছে কিনা
#         if amount > self.balance:
#             print(f"Failed to withdraw {amount}. You don't have enough money!")
#         else:
#             # ব্যালেন্স থাকলে এখন টাকা কাটবো
#             self.balance -= amount
#             print(f"{amount} Taka withdrawn. Current Balance: {self.balance}")
#
# # Testing
# my_account = BankAccount("Mamun")
#
# # ১০০ টাকা জমা দিলাম
# my_account.deposit(100)
#
# # ২০০ টাকা তুলতে চাইলাম (কিন্তু আছে ১০০ টাকা)
# my_account.withdraw(200)

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} Taka deposited. Balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"{amount} Taka withdrawn. Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.5
        self.balance += interest
        print(f"Interest added! New balance: {self.balance}")

my_savings_account = SavingsAccount("Mamun")
my_savings_account.deposit(1000)
my_savings_account.add_interest()
my_savings_account.withdraw(500)
