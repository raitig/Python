class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class manager(Programmer):
    c = 3

o = Employee()
print(o.a) #Prints the a attributte
#print(o.b) # Shows an error as there is no b attribuite in Employee class

o = Programmer()
print(o.a, o.b) #Prints the a and b attributtes

o = manager()
print(o.a, o.b, o.c) #Prints the a, b and c attributtes