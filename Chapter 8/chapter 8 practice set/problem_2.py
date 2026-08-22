''' Write a python program using function to convert Celsius to Fahrenheit.
Celsius to Fahrenheit Formula: C/5 = (F-32)/9
'''
def c_to_f(u):
    return 5*(u-32)/9

u = int(input("Enter temperature in Celsius : "))
print(c_to_f(u))