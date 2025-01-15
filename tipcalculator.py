print("Welcome to the tip calculator")

while True:
    totalBill = float(input("Enter the total bill:"))
    gorjeta = int(input("How much tip wold you like to give: "))
    people = int(input("How many people to split the bill: "))
    quit = str(input("Enter q for quit: "))
    if quit == "q":
        break

gorjeta2 = totalBill * (gorjeta / 100)
totalBill = totalBill + gorjeta2 
total = totalBill / people
print(f"Each person should pay {round(total, 2)}")
