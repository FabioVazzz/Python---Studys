menu = {"pizza": 3.00, "nachos": 4.50, "popcorn": 6.00, "fries": 2.50, "chips": 3.00, "pretzel": 3.50, "soda": 3.00, "lemonade": 4.25}

buy = []
total = 0


print('=============== MENU ===============')
for prod, price in menu.items():
  print(f'{prod:10}: {price:.2f}')
print('====================================')


while True:
    Buy = input("Enter the name of product you wnat to buy: (q/quit)")
    if Buy == "q":
       break
    elif Buy in menu:
       buy.append(Buy)
    
for items in buy:
   total += menu[items]

print(f"The total of your cart is: {total}")