#Temperature conversion program

temperature = str(input("Enter your unity of temperature (C or F): "))
value = float(input("Enter the temperature: "))

if temperature == "C":
    total = (value * 9) /5 + 32
    print(f"Your temperature in celsius is: {round(total, 2)}")
elif temperature ==  "F":
    total = (value - 32) * 5/9
    print(f"Your temperature in fahrenheit is: {round(total, 2)}")
else:
    print("Enter valid unity")