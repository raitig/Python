class Employee:
    a = 1
    @classmethod #A class method works with the class itself, not individual objects. It uses cls instead of self.
    def show(cls):
        print(f"The Class attribute of a is {cls.a}")
e = Employee()
e.a = 45
e.show()
