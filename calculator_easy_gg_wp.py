number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))
operation_to_do = input("Operation: ")

if operation_to_do == "/":
    if number_2 == 0:
        print("Division by zero is impossible")
    else:
        result = number_1 / number_2
        print("Result: ", result)

if operation_to_do == "+":
    result = number_1 + number_2
    print("Result: ", result)

elif operation_to_do == "-":
    result = number_1 - number_2
    print("Result: ", result)

elif operation_to_do == "*":
    result = number_1 * number_2
    print("Result: ", result)

