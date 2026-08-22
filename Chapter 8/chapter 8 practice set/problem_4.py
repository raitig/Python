# Write a recursive function to calculate the sum of first n natural numbers.
''' EX:
sum(1) = 1
sum(2) = 1 + 2 
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = 1 + 2 + 3 + 4 + 5 + ... + n '''
u = int(input("Enter a number : "))
def sum(n):
    if (n == 1):
        return 1
    return sum(n - 1) + n
print("Sum of first", u, "natural numbers is:", sum(u))