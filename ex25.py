import random

ramdomNumber = random.randint(1, 10)


while True:
    guess = int(input("Enter the number you think is the correct number: "))
    if guess == ramdomNumber:
        print("Correct number")
        break
    elif guess < ramdomNumber:
        print("WRONG")
        print("Your number is lower than the correct number")
    elif guess > ramdomNumber:
        print("WRONG")
        print("Your number is high than the correct number")
    else:
        print("Not number correct")