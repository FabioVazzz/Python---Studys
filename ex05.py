#if = do some code only IF some condition is true 
#Else do something else

age = int(input("Whats your age?: "))

#se
if age >= 18:
    print("You are now sign up!")
#senao se
elif age < 0:
    print("You haven't been born yet")
#senao
else:
    print("You must be 18+ to sign up")