try: #exception handling is a mechanism in programming that allows you to handle errors or exceptional situations that may occur during the execution of a program. It helps prevent the program from crashing and allows you to gracefully handle errors.
    a = int(input("Hey, Enter a number : ")) # Exception handeling start with try block. The code that may raise an exception is placed inside the try block. In this case, we are trying to convert the user input into an integer using the int() function. If the user enters a valid number, it will be converted successfully and assigned to the variable 'a'.
    print(a)
except Exception as e:
    print("Error : ", e)

print("Thank you")