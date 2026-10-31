def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2
option = ''
while option != 'exit':
    enter = input("Do you want to perform a calculation? (yes/no): ")
    if enter.lower() != 'yes':
        print("Exiting the calculator.")
        break
    select = input("Select operation ( 1 add, 2 subtract, 3 multiply, 4 divide): ")
    if select in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if select == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif select == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif select == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif select == '4':
            try:
                result = divide(num1, num2)
                print(num1, "/", num2, "=", result)
            except ValueError as e:
                print(e)
option = input("Do you want to perform another calculation? (yes/no): ")
if option.lower() != 'yes':
    print("Exiting the calculator.")
    option = 'exit'
