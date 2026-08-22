class Employee: #here is Employee is class 
    language = "python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")

    @staticmethod # This is now aesthetic method in Python is a method that belongs to the class but does not use the instance (self) or the class (cls) 
    def greet():
        print("Good Morning")
Raitig = Employee() # This is tyhe Instance arttribute \
# Raitig.language = "machine Learning"
# print(Raitig.language, Raitig.salary)
Raitig.getInfo()
Raitig.greet()