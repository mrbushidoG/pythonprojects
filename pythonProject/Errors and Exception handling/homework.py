# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except TypeError:
#     print("You are using an integer instead of string")


# x = 5
# y = 0
# try:
#     z = x/y
# except ZeroDivisionError:
#     print("Division by zero not allowed")
#
# finally:
#     print("Get your math right")
# print(type(23))
def ask():
     while True:
             try:
                 number = int(input("Please enter a number to be squared "))
             except:
                 print("Error you did not enter a number please enter a number")
                 continue
             else:
                 print(f"Thank you for your input, the square of the number is {number**2}")
                 break

ask()
