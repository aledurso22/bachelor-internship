import unittest
from lattice import Lattice

class TestLatticeInitialization(unittest.TestCase):
    
    def test_initialization_n_leq_l(self):
        # Test cases where N <= L
        print("Test case where N <= L:")
        lattice = Lattice(10, 5)
        lattice.initialization()
        result = lattice.get_combined()
        print(f"Combined array: {result}")
        self.assertIsNotNone(result, "Initialization failed for N <= L")
        
        # Check if the middle position contains a 1
        middle_index = len(result) // 2
        if len(result) % 2 == 0:  # Even length
            self.assertTrue(result[middle_index] == 1 or result[middle_index - 1] == 1, "Neither of the middle positions have a 1")
        else:  # Odd length
            self.assertTrue(result[middle_index] == 1, "Middle position does not have a 1")
        
        print("Test passed for N <= L\n")
    
    def test_initialization_n_gt_l(self):
        # Test case where N > L
        print("Test case where N > L:")
        with self.assertRaises(ValueError) as context:
            lattice = Lattice(5, 10)
            lattice.initialization()
        self.assertEqual(str(context.exception), "The number of -1's (N) must not exceed the number of zeros (L).", "Incorrect error message")
        print("Caught expected ValueError:", context.exception)
        print("Test passed for N > L\n")
    
    def test_middle_one(self):
        """
        Test that there is a 1 in the middle of the array if N >= 1.
        """
        print("Test case to check if there is a 1 in the middle:")
        
        # Test for odd total length
        lattice = Lattice(9, 5)
        lattice.initialization()
        result = lattice.get_combined()
        middle_index = len(result) // 2
        self.assertTrue(result[middle_index] == 1, "Middle position does not have a 1 in an odd length lattice")
        print(f"Combined array with odd length: {result}")
        
        # Test for even total length
        lattice = Lattice(10, 5)
        lattice.initialization()
        result = lattice.get_combined()
        middle_index1 = len(result) // 2
        middle_index2 = middle_index1 - 1
        self.assertTrue(result[middle_index1] == 1 or result[middle_index2] == 1, "Neither of the middle positions have a 1 in an even length lattice")
        print(f"Combined array with even length: {result}")

if __name__ == '__main__':
    unittest.main()
