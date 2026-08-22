class employee:
    company = "Google"
    def show(self):
        print(f"The name of the employye is {self.name} and the salary is {self.salary}")

# class progmmer:
#     company = "Youtube"
#     def getinfo(self):
#         print(f"The name of the employye is {self.name} and the salary is {self.salary}") 
#     def showlanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
class programmer(employee):
     company = "Youtube"
     def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
a = employee()
b = programmer()
print(a.company, b.company)