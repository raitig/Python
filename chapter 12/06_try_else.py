def main():
    try:
        a = int(input("Hey, Enter a number : ")) # Exception handeling start with try block. The code that may raise an exception is placed inside the try block. In this case, we are trying to convert the user input into an integer using the int() function. If the user enters a valid number, it will be converted successfully and assigned to the variable 'a'.
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally: # Finally block return when the function is used and try block is executed successfully or when an exception is raised. The code inside the finally block will always be executed, regardless of whether an exception occurred or not. In this case, we are printing a message indicating that no exception occurred.
        print("No exception occurred.")

main()