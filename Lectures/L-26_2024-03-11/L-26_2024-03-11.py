# SOLID Principles

# The Single Responsibility Principle (SRP)

# The SRP comes from Robert C. Martin founder of the term SOLID

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

# Example of using FileManager clas s

file_manager = FileManager("Lectures/L-26_2024-03-11/example.txt")
print(file_manager.path)
file_manager.write("Hello, World")
print(type(file_manager.read()))
print(file_manager.read())
