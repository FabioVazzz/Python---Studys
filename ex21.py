#shopping cart program

fruits = []
prices = []
total = 0

while True:
    fruit = str(input("Enter your product (q/quit): "))
    if fruit == "q":
        break
    fruits.append(fruit)
    price = int(input("Enter price: (q/quit): "))
    prices.append(price)

print("-------Your Items-------")

for fruit in range(len(fruits)):
    print(f"Your product is: {fruits[fruit]}, and your price is: {prices[fruit]}")

for price in range(len(prices)):
    total += prices[price]

print(f"The total of your buy is: {total}")
