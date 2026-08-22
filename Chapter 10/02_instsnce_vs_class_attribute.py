class Employee: #here is Employee is class 
    language = "python"
    salary = 1200000

Raitig = Employee() # This is tyhe Instance arttribute 
Raitig.language = "machine Learning" # Instant attribute Take preference over class attribute during assignment and retrieval.
print(Raitig.language, Raitig.salary)
# !st check the instance attribute if doesn't have the instance attribute to print the class attribute. If have the instance attribute attribute so print the instance attribute.