initial_balance = 0
interest_rate = 0
installments = 0

while initial_balance <= 0:
    initial_balance = float(input('enter the inicial balance:'))
    if initial_balance <= 0:
        print('initial balance cant be 0 or negative')

while installments <= 0:
    installments = int(input('enter the installments:'))
    if installments <= 0:
        print('initial_balance cant be 0 or negative')

while interest_rate <= 0:
    interest_rate = float(input('enter the rate:'))
    if interest_rate <= 0:
        print('interest rate cant be 0 or negative')

final_balance = initial_balance * pow((1 + interest_rate / 100), installments)
print(f'in {installments} you will have {final_balance:.2f}')