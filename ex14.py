# format specifiers = {value:flags} format a value based on what
# flags are inserted 

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align 
# :+ = use a plus sign to indicate positive value
# := place sign to leftmost position
# :  = insert a space before positive numbers 
# :, = comma separator 

price1 = 3.14159

print(f"Price 1 is ${price1:^10}")