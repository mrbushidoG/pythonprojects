from packages.main import mathme

def arithmetic_operations():
    operation_type = input("Please enter if you want to add, multiply or divie\n")

    if operation_type == "add":
        number1 = input("Please enter your first number\n")
        number2 = input("Please enter your second number\n")
        return mathme.add_numbers((int)(number1),(int)(number2))
    elif operation_type =="multiply":
        number1 = input("Please enter your first number\n")
        number2 = input("Please enter your second number\n")
        return mathme.multiply_numbers((int)(number1),(int)(number2))
    else:
        number1 = input("Please enter your first number\n")
        number2 = input("Please enter your second number\n")
        return mathme.divide_numbers((int)(number1),(int)(number2))

if __name__ == '__main__':
    print("Runnin from main")
    result = arithmetic_operations()
    print(f"The Result is {result}")
else:
   print("Runnin not from main")
   result = arithmetic_operations()
   print(f"The Result is {result}")
