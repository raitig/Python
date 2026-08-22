# Write a program using functions to find greatest of three numbers.
def greatest(a ,b, c):
    if ((a > b) and (a > c)):
        return a
    elif((b > a) and (b > c)):
        return b
    else:
        return c 
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
print(f"The greatest of the three numbers is : {greatest(a, b, c)}")