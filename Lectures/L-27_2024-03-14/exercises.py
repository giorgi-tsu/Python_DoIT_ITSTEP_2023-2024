import unittest

def equal_lists(list1, list2):
    return list1 == list2


class TestListsEquality(unittest.TestCase):
    def test_equal_lists(self):
        list1 = [2, 4, 7]
        list2 = [2, 4, 7]

        self.assertTrue(equal_lists(list1, list2), "The lists are different")

if __name__ == "__main__":
    unittest.main()