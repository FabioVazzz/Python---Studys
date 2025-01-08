#Python calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = str(input("Enter the operation you want to perform: "))

if operation == "+":
    total = num1 + num2
elif operation == "-":
    total = num1 - num2
elif operation == "*":
    total = num1 * num2
elif operation == "/":
    total = num1 / num2
else:
    print("Select a operation valid")

print(f"Your result is: {total}")
