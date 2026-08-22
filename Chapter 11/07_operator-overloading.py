class number:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n
    def __sub__(self, other):
            return self.n - other.n
    def __mul__(self, other):
        return self.n * other.n
    def __truediv__(self, other):
        return self.n / other.n
    def __floordiv__(self, other):
        return self.n // other.n
n = number(5)
m = number(10)

print(n + m) #This will give an error because the + operator is not defined for the number class. To fix this, we can overload the + operator by defining a __add__ method in the number class.
print(n - m) #This will give an error because the - operator is not defined for the number class. To fix this, we can overload the - operator by defining a __sub__ method in the number class.
print(n * m) #This will give an error because the * operator is not defined for the number class. To fix this, we can overload the * operator by defining a __mul__ method in the number class. 
print(n / m) #This will give an error because the / operator is not defined for the number class. To fix this, we can overload the / operator by defining a __truediv__ method in the number class.
print(n // m) #This will give an error because the // operator is not defined for