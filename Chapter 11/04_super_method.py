#class Employee:
#     def __init__(self):
#         print("Constructor of Employee")
#         a = 1
# class programmer(Employee):
#     def __init__(self):
#         print("constructor of Programmer")
#         b = 2
# class Manager(programmer):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of Manager")
#         c = 3
# # o = Employee()
# # print(o.a)

# # o = programmer()
# # print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)
class Employee:
    def __init__(self): #self refers to the current object (instance) of a class. It allows you to access the instance's variables and methods.
        print("Constructor of Employee")
        self.a = 1

class Programmer(Employee):
    def __init__(self): # Self means one object where is the 
        super().__init__()
        print("Constructor of Programmer")
        self.b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
        self.c = 3

o = Manager()
print(o.a,o.b, o.c)
