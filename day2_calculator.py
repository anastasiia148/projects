def add (a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide (a,b):
    return a/b

again = "yes"
while again == "yes":
    
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    if operation == "+":
        print(add(first_number, second_number))
    elif operation == "-":
        print(subtract(first_number, second_number))
    elif operation == "/":
        if second_number == 0:
            print("Cannot divide by 0")
        else:
            print(divide(first_number, second_number))
    elif operation == "*":
        print(multiply(first_number, second_number))
    else:
        print("Invalid operation.")
    again = input("Do you want to continue? yes/no: ")
