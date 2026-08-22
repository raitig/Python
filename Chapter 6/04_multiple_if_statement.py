a = int(input("Enter you age :"))

# If statement no 1:
if(a % 2 == 0):
    print("You are entering the even number")
if (a % 2 != 0):
    print(" You are enter the odd number")
# End of if statement no 1

# If statement no 2 
if(a>=18):
    print("You are above the age of consent")

elif(a<0):
    print("You are entering an negative age.")

elif(a==0):
    print("You are entering an zero wich is not a valid age.")

else : 
    print("You are below the age of consent")

# End of if statement no 2

print("End of this program")