# while loop = execute some code WHILE some condition remains true

age = int(input("Whats your age ?: "))

while age < 0:
    print("Age can't be a negative")
    age = int(input("Whats your age ?: "))

print(f"You are {age} years old")