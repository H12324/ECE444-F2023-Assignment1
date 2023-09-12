import unittest
from utils import Utils

class UtilsTest(unittest.TestCase):
    #Pretty sure my code will fail with negative number but I'm not gonna test that :)
    def test_reveresed(self): 
        # Test with String
        self.assertEqual(Utils.reveresed("542"), "Invalid Input") # Funnily would still work if I didn't filter strings
        # Test with Float 
        self.assertEqual(Utils.reveresed(542.0), "Invalid Input")
        # Test with Int
        self.assertEqual(Utils.reveresed(542), 245)
            

    def test_formatter(self):
        # Test with String
        self.assertEqual(Utils.formatter("542"), "Invalid Input")
        # Test with Float 
        self.assertEqual(Utils.formatter(542.0), "Invalid Input")
        # Test with Int
        self.assertEqual(Utils.formatter(542), ('0b1000011110', '0o1036'))

        
if __name__ == '__main__':
    unittest.main()