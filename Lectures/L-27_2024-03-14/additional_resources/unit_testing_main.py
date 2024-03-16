# This script is based on the following video:

# https://www.youtube.com/watch?v=6tNS--WetLI

# Plan of the tutorial:

# 1. How to write tests
# 2. How to setup and tear down your tests
# 3. Review some best practices

# A good test saves a lot of time and headache down the road.

# When you write good tests for your code, it gives you more 
# confidence that your updates and refactoring don't have any 
# unintended consequences or break your code in any way. So,
# for example, if you update a function in your project, 
# those changes may have actually broken down several 
# sections of your code even if that function itself 
# is still working. Good unit tests will make sure everything 
# is working as it should if it's not then it will show exactly 
# what's broken.

# In this tutorial will cover the built-in unittesting module:
# unittest

# Steps for unit testing:

# 1. Create a test module

  # Create a new file and call it "test_file.py", where file is the
# name of the file that you are testing. In this case it is 
# "test_calc.py" since we are testing "calc.py"

# 2. import unittest module

  # import unittest

# 3. import the module you want to test

  # import file.py

# 4. Create test cases

  # We need to create some test cases for the functions
# that we want to test. To create those test cases we first need
# to create a test class that inherits from "unittest.TestCase".
# It is recommended to give a descriptive name to this like. 
# For example, class TestCalc(unittest.TestCase)...

# 5. Start writing methods for tests

  # It is required that each test method starts with "test_".
# For example, "test_add" to test "add" function. This is required
# because when we ran the class it actually knows which methods
# represent tests. So, if the method does not start with the "test_"
# then it won't be run.

# Here is the link for the description of all the asserts
# inherited from the unittest.TestCase:

# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug 

