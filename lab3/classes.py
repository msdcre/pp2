# ex1
# class StringManipulator:
#     def __init__(self):
#         self.input_string = ""
#     def getString(self):
#         self.input_string = input("Enter a string: ")
#     def printString(self):
#         print("String in uppercase:", self.input_string.upper())
# string_manipulator = StringManipulator()
# string_manipulator.getString()
# string_manipulator.printString()

# ex2
# class Shape:
#     def __init__(self):
#         pass 
#     def area(self):
#         return 0 
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length
#     def area(self):
#         return self.length * self.length  
# shape_instance = Shape()
# print("Area of Shape:", shape_instance.area())  
# square_instance = Square(8)
# print("Area of Square:", square_instance.area())

# ex3
# class Shape:
#     def __init__(self):
#         pass 
#     def area(self):
#         return 0  
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__()  
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# rectangle_instance = Rectangle(4, 6)
# print("Area of Rectangle:", rectangle_instance.area())  


# ex4
# import math
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(f"Coordinates of the point: ({self.x}, {self.y})")
#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#     def dist(self, other_point):
#         distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
#         return distance
# point1 = Point(2, 3)
# point2 = Point(5, 7)
# point1.show() 
# point2.show()  
# point1.move(4, 6)
# point1.show()
# distance_between_points = point1.dist(point2)
# print(f"Distance between the points: {distance_between_points}")


# ex5
# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposit of {amount} successfully made. New balance: {self.balance}")
#         else:
#             print("Invalid deposit amount. Please enter a positive amount.")
#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 print(f"Withdrawal of {amount} successfully processed. New balance: {self.balance}")
#             else:
#                 print("Insufficient funds. Withdrawal canceled.")
#         else:
#             print("Invalid withdrawal amount. Please enter a positive amount.")
# account1 = Account("John Doe", 1000)
# account1.deposit(500) 
# account1.withdraw(200)  
# account1.deposit(-100)  
# account1.withdraw(1500) 
# account1.withdraw(-50) 

# ex6
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# numbers=input().split()
# prime_numbers = list(filter(lambda x: is_prime(int(x)), numbers))
# print(prime_numbers)
