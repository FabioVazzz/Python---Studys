#Weight conversion program

Weight = float(input("Enther your weight: "))
Unity = str(input("Enther your unity (pounds ou kilograms): "))

if Unity == "pounds":
    total = Weight * 2.205
    print(f"Your weight is: {round(total, 2)}")
elif Unity == "kilograms":
    total = Weight / 2.205
    print(f"Your weight is: {round(total, 2)}")
else:
    print("Enther a valid unity please!")