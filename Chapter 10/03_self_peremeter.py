class Employee: #here is Employee is class 
    language = "python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")

    def greet(self):
        print("Good Morning")
Raitig = Employee() # This is tyhe Instance arttribute \
Raitig.language = "machine Learning"
print(Raitig.language, Raitig.salary)
Raitig.getInfo()
Raitig.greet()