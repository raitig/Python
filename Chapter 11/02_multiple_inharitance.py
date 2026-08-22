class employee:
    company = "Google"
    name = "Raitig"
    def show(self):
        print(f"The name of the employye is {self.name} and the company is {self.company}")

class coder:
    language = "python"
    def printlanguages(self):
        print(f"Out of the all languages here is your language {self.language}")
   
class programmer(employee, coder):
     company = "Youtube"
     def showlanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
a = employee()
b = programmer()
b.show()
b.printlanguages()
b.showlanguage()