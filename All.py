# Write a program to add teo numbers
a = int(input("Enter the first number : "))
b = int(input("Enter the second number :"))
print(a+b); 


# Write a program to find the remainder when a number is divided by Z
a = int(input("Enter the 1st number :"))
z = int(input("Enter the 2nd number :"))
print(a%z) 


# write a program to check the type of vriable assigned using input function 
a = (input("Type anything : "))
print("value",a)
print("type",type (a)) 


# Write a program use comparison operator to find out whether 'a' given variable a is greater than 'b' or not .
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number :"))
if a > b :
    print("a is greater then b.")
elif a < b :
    print("b is greather then a. ")
elif a == b :
    print("a is equal to b.")
else:
    print("Nothing.") 


# Write a python program to find an average of two numbers entered by the user 
num1 = int(input("Enter your 1st number :"))
num2 = int(input("Enter your 2nd number :"))
average = (num1 + num2)/2 ; 
print("Two number of average is : ",average)


# Write a python program to calculate the square of a number entered by the user.
num = float(input("Enter the number :"))
square = num ** 2   # (also we can use this line Square = num * num)  
print(f"number of square {num} is {square}")


# Write a python program to display a user entered name followed by good afternoon using input() function 
Who = input("Enter your name : ")
print("Good morning,", Who )


# Write a program to fill in a letter template given below with name and date 
letter = """ Dear <|Name|>,
         you are selected ! 
        <|Date|> """
Name = input("Enter your name:")
Date = input("Enter the date:")
letter = letter.replace("<|Name|>",Name)
letter = letter. replace("<|Date|>", Date)
print(letter)


# Write a program to detect double space in a string
a = input("Enter your string :")
if "  " in a :
    print("Double space is detected....!")
else :
    print(" Dosen't detected the Double space.....!")


# Replace the double space from problem 3 with single space 
a = input("Enter your string :")
b = a.replace(" " , " ")
print("After", a)
print("Before",b)


# Write a program to sort the list 
list = [2,6,5,1,8,90,34,32,67]
list.sort()
print(list)


# Write a program to reverse the list
list = [2,6,5,1,8,90,34,32,67]
list.reverse()
print(list)


# Write a program to append the list 
list = [2,6,5,1,8,90,34,32,67]
list.append(100)
print(list)


# Write a program to insert the list 
list = [2,6,5,1,8,90,34,32,67]
list.insert(7,3)
print(list)


# Write a program to pop the list
list = [2,6,5,1,8,90,34,32,67]
list.pop()
print(list)


# Write a program to remove the list 
list = [2,6,5,1,8,90,34,32,67]
list.remove(90)
print(list)
