# SOLID Principles

# 1. The Single Responsibility Principle (SRP)

# The SRP comes from Robert C. Martin, the founder of the term SOLID.

# The SRP states: "A class should have only one reason to change"

# This means that a class should have only one responsibility, as
# expressed through its methods. If a class takes care of more than
# one task than you should seperate those tasks into classes.

from pathlib import Path
from zipfile import ZipFile

# The class below violates SRP because it has two different 
# responsibilities. One is using .read() and .write() for managing 
# the file and another is using .compress() and .decompress() for 
# dealing with ZIP archives.

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)
    
    def write(self, data,  encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


# Using FileManager class

file_manager = FileManager("Lectures/L-26_2024-03-11/example.txt")
print(file_manager.path)
file_manager.write("Hello, World!")
print(type(file_manager.read()))
print(file_manager.read())

# Splitting the FileManager class into two smaller, more focused
# classes, each with its own specific concerns:

class FileManager:

    def __init__(self, filename):
        self.path = Path(filename)
    
    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)
    
    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)


# Using FileManager class

file_manager = FileManager("Lectures/L-26_2024-03-11/"\
                           "example_SRP.txt")
print(file_manager.path)
file_manager.write("Hello, World with SRP!")
print(type(file_manager.read()))
print(file_manager.read())


class ZipFileManager:

    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


# Need to understand using ZipFIle later


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
            print(kwargs)
            print(type(kwargs))
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

# Example of using the Shape class that violates the OCP.
            
from shapes_ocp import Shape

rectangle = Shape("rectangle", width=10, height=5)
print(rectangle.calculate_area())

circle = Shape("circle", radius=5)
print(circle.calculate_area())


from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type
    
    @abstractmethod
    def calculate_area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius =radius

    def calculate_area(self):
        return pi * self.radius ** 2

circle = Circle(radius=5)
print(circle.calculate_area())