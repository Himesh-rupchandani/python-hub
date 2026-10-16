# age = 15
# if age<18:
#     raise NameError("age must be above 18")

# x= 'hello'
# if not type(x) is int:
#     raise TypeError("Only integer is allowed")

# cgpa = 5.5
# if cgpa<6.5:
#     raise Exception("Cgpa is ...")

# x = int(input("Enter value of x="))
# y = int(input("Enter value of y="))

# try:
#     result = x/(x-y)
# except ZeroDivisionError:
#     print("Division by zero")
# finally:
#     print("executing final clause")

# Q. Write a python program that asks the user to enter two numbers. the program should validate the inputs using exception handling to ensure that only valid numeric value are excepted once two valid number are entered ,calculate and display their product.

# def get_number(msg):
#     while True:
#         try:
#             return float(input(msg))
#         except ValueError:
#             print("Invalid input. Enter a number.")


# def main():
#     try:
#         a = get_number("Enter first number: ")
#         b = get_number("Enter second number: ")

#         ans = a * b

#         print("The product is:", ans)

#     except Exception as e:
#         print("Error:", e)

#     finally:
#         print("Program finished.")


# main()

# write a python program that executes an operation on alist and handles an indexerror Exception if the index is out of range.
# simple program to show index error handling

# program to handle index error with retry

my_list = [10, 20, 30, 40, 50]

while True:
    try:
        index = int(input("Enter the index: "))
        print("Element at index", index, "is:", my_list[index])
        break   
    except IndexError:
        print("index is not in the list. Please enter again.")

print("Program continues after handling exception...")