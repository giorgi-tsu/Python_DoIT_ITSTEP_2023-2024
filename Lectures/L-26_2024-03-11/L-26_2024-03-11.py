# SOLID Principles

# The Single Responsibility Principle (SRP)

# The SRP comes from Robert C. Martin founder of the term SOLID

# The SRP states: "A class should have only one reason to change"

# This means that a class should have only one responsibility, as
# expressed through its methods. If a class takes care of more than
# one task than you should seperate those tasks into classes.

from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="urf-8"):
        return self.path.read_text(encoding)
    
    def write(self, data,  encoding="urf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
