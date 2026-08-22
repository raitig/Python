# This is the function with argument that means we can pass the value to the function and it will print the value that we passed to it.
# def goodday(Name, ending): # Here is the (name) is a parameter where is can pass the (Raitig) Nmae a as value. 
#     print("Good day, " + Name) # + sign is used to concatenate the string with the varrible name.
#     print(ending)
# goodday("Raitig", "Thank you")
# goodday("Disha", "Thanks")
# goodday("Gourab", "Thank you")
# goodday("Soumili", "Thanks")
# goodday("Debajit", "Thank you")
# goodday("pratyasha", "Thanks")
# goodday("Bijoy", "Thank you")
# goodday("Suchishmita", "Thanks")


def goodday(Name, ending): # Here is the (name) is a parameter where is can pass the (Raitig) Nmae a as value. 
    print("Good day, " + Name) # + sign is used to concatenate the string with the varrible name.
    print(ending)
    return "Ok" # return means function you can carry some value and paste this value in the varrible. We can use the return at the one time for one varrible.
a = goodday("Raitig", "Thank you")
print(a)