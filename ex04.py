#Mathmatics functions
import math

#EXERCICE 1
print("Lets to calculate the circumference of a circle") 
radius = float(input("Enther the radius of a circle: "))

circle = 2 * math.pi * radius

print(f"The circumference of a circle is: {round(circle, 2)}")

###########

#EXERCISE 2
radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area is: {round(area, 2)}")

###########

#EXERCISE 3
a = float(input("Enter the cateto a value: "))
b = float(input("Enter the cateto b value: "))

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"The hipotenusa is: {round(c, 2)}")

x = 3.14
y = 4
z = 5
#Arredonda o valor 
result = round(x)

#Distancia ate 0 do valor
result = abs(y)

#Faz o exponencial
result = pow(4,3)

#Pega o valor maximo das variaveis
result = max(x, y, z)

#Pega o valor minimo das variaveis
result = min(x, y, z)

#Faz a raiz quadrada
result = math.sqrt(x)

#Arredonda para cima
result = math.ceil(x)

#Arredonda para baixo
result = math.floor(x)