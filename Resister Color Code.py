color = ["black", "brown", "red", "orange", "yellow", "grenn", "blue", "violet", "grey", "white"]

n=color.index((input("Enter the first color: ")))
m=color.index((input("Enter the second color: ")))
p=color.index((input("Enter the third color: ")))

q=int(((n*10)+(m))*(10**(p)))
z=q/1000


print("The resister value Is: ")
print(f"{q}Ω and in Kiloohm : {z}kΩ")