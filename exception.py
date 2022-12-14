# # ValueError
# import math
# x = int(input("Please enter a positive number: "))
# try:
#     print(f"Square Root of {x} is {math.sqrt(x)}")
# except ValueError as ve:
#     print(ve)
#     print(f"You entered {x}, which is not a positive number.")

# # # ArithmeticError
# try:
#     11/0
# except ArithmeticError as e:
#     print(e)
#     print("This is an example of catching ArithmeticError.")

# # # IOError
# try:
#     file = open("sample.txt", "w")
#     print("File found.")

# except IOError:
#     print("File not found.")

# # ImportError
# try:
#     from exception import robocon
# except Exception as e:
#     print(e)

# # # NameError
# def m():
#     try:
#         name = "Riya"
#         return lname
#     except NameError:
#         return "NameError occured. Variable undefined"
        
# print(m())

# # User defined
class Mistake(Exception):
    pass

marks = int(input("Enter marks: "))
if marks < 0 or marks > 100:
    raise Mistake("Wrong marks entered.")