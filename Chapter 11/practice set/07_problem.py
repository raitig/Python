# Override the __len__() method on vextor of problem 5 to display the dimension to the vector 

# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)
      

# Test the implement
v1 = vector([1, 2, 3])
print(len(v1)) # Output: 3