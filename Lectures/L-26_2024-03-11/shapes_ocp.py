# 2. The Open-Closed Principle (OCP)

# The open-closed principle for object-oriented design was first
# introduced by Bertrand Meyer in 1988 and means that:

# "Software entities (classes, modules, functions, etc.) should
# be open for extension but closed for modification." 

from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius ** 2


# The Shape class above violates the OPC because if you need to add
# a new shape, for example, square, you must modify the internal
# code of the class. For example, you need to add another elif 
# clause to  .__init__() and to .calcualte_area() so that you can
# address the requirements of a square shape.  

# Having to make these changes to create new shapes measn that your
# your class is open for modification. Here is a possible solution 
# to fix your class to make it open for extension but closed for 
# modification:
        