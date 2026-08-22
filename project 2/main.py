'''we are going to write a program that generate a random number and asks the user to guess it. 
If the player's guess is higher then the actual number, the program display "Lover number please". Similarly, if the user's guess is too low, the program prints "Higher nuber please" when the user guesses the correct number, the program displays the number of guesses the player used to arrive at rh number.
Hint - use the random module'''
import random 
n = random.randint(1, 100)
a = -1
guesses = 1
while (a != n):
    a = int(input("Guess a number: "))
    if(a > n):
        print("lower number please")
        guesses += 1
    elif(a < n):
        print("Higher number plaese")
        guesses += 1  

print(f"You have guessed the number {n} correctly in {guesses} attempts")