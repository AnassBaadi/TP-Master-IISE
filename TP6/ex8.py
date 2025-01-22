import unittest
from ex1 import safe_division

class test(unittest.TestCase):
    def test_read_file(self):
        with self.assertRaises(ZeroDivisionError):
             safe_division(21,0)

if __name__ == "__main__":
    unittest.main()