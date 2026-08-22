class Employee:
    a = 10 #Class attribute

    @classmethod #A class method works with the class itself, not individual objects. It uses cls instead of self.
    def show(cls):
        print(f"The Class attribute of a is {cls.a}")

    @property #A property decorator allows you to define a method that can be accessed like an attribute. It is used to create read-only attributes or computed properties.
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter #A setter decorator allows you to define a method that can be used to set the value of a property. It is used to create writable attributes or computed properties.
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45
e.name = "Raitig Sarkar"
print(e.fname, e.lname)

e.show()