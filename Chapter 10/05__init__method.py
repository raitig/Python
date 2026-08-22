class Employee: 
    language = "python"
    salary = 1200000

    def __init__(self, name, salary, language): # it is a method which is automatically called. In this method we can also say in python (Dunder method)
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

Raitig = Employee("Raitig", 1500000, "Machine Learning")
# Raitig.name = "Raitig"
print(Raitig.name, Raitig.salary, Raitig.language)