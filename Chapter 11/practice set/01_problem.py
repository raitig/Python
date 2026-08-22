# Creating a class (2-D vector) and use it to create another class representing a 3-D vector.
class Vector2D:
    def __init__(self, x, y): # This is a constructor method that initializes the x and y coordinates of the 2-D vector to 0.
        self.x = x
        self.y = y

    def show(self): # This is a method that prints the x and y coordinates of the 2-D vector.
        print(f" The Vector is {self.x}, {self.y} y") # This line prints the x and y coordinates of the 2-D vector.

class Vector3D(Vector2D): # This line defines a new class called Vector3D that inherits from the Vector2D class.
    def __init__(self, x, y, z): # This is a constructor method that initializes the x, y, and z coordinates of the 3-D vector to 0.
        super().__init__(x, y) # This line calls the constructor of the parent class (Vector2D) to initialize the x and y coordinates of the 3-D vector.
        self.z = z
    def show(self): # This is a method that prints the x and y coordinates of the 2-D vector.
            print(f" The Vector is {self.x}, {self.y}, {self.z} z") # This line prints the x and y coordinates of the 2-D vector.

a = Vector2D(1, 2) # This line creates an instance of the Vector2D class with x=1 and y=2.
b = Vector3D(3, 4, 5) # This line creates an instance of the Vector3D class with x=3, y=4, and z=5.
a.show()
b.show()