#Logical operators = evaluate multible condition (or, and, not)


temp = 25
is_sunny = True
is_raining = True


if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")

if temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")