import numpy as np

class Lattice:
    def __init__(self, L: int, N: int) -> None:
        """
        Initialize the Lattice with the number of zeros (L) and the number of -1's (N).
        
        :param L: Number of zeros to be placed randomly.
        :param N: Number of -1's to be placed randomly.
        """
        if N > L:
            raise ValueError("The number of -1's (N) must not exceed the number of zeros (L).")
        
        self.L = L
        self.N = N
        self.combined = None  # Initialize the combined variable to None
    
    def initialization(self) -> None:
        """
        Create an array with N -1's and L zeros, ensuring a 1 in the middle position.
        """
        total_length = self.L + self.N
        
        if self.N > 0:
            middle_index = total_length // 2
            
            # Create an array with (N) -1's
            minus_ones = np.full(self.N, -1)

            # Create an array with L zeros
            zeros = np.zeros(self.L)

            # Combine zeros and -1's
            combined_array = np.concatenate((minus_ones, zeros))
            
            # Insert a 1 in the middle position (which is a zero)
            combined_array = np.insert(combined_array, middle_index, 1)

            # Shuffle the array, excluding the middle position which is 1
            self.combined = np.roll(combined_array, 1)  # Roll the array to the right
            self.combined[middle_index] = 1  # Ensure the middle position remains 1

            # Shuffle other elements
            np.random.shuffle(self.combined[:middle_index])  # Shuffle left of the middle
            np.random.shuffle(self.combined[middle_index + 1:])  # Shuffle right of the middle

        else:
            # If N is 0, just return an array of zeros
            self.combined = np.zeros(self.L)
    
    def get_combined(self) -> np.ndarray:
        """
        Return the combined array if it exists.
        
        :return: The combined array of -1's and zeros.
        """
        if self.combined is None:
            raise ValueError("The array has not been initialized yet. Call initialization() first.")
        
        return self.combined
