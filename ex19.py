# neted loop = A loop within another lop (outer, inner)
# outer loop:
#   inner loop:

rows = int(input("Enter the # of rows: "))
colums = int(input("Enter the # of columns"))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(colums):
        print(symbol, end="")
    print()