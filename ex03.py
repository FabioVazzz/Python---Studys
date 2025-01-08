#input() = A function that prompts the user to enter data
#Return the entered data as a string

age = int(input("Whats your age?: "))
age = age + 1


print(f"You have a {age} years old")

#Exercise 1
lenght = int(input("Enter the lenght: "))
width = int(input("Enter the width: "))

area = lenght * width 

print(f"The area is {area}")

#Exercise 2 

item = input("What item would you like to buy?: ")
price = float(input("Enter price of the product: "))
quantity = int(input("Enther the quantity of product: "))

total = price * quantity

print(f"The name of the product is: {item}, The price is: {price}, The quantity is: {quantity}, The total of your buy is: {total}")
