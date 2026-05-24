import numpy as np
def random_array(shape, low=0, high=1):
    """
    Generate a random array with the specified shape and value range.

    Parameters:
    shape (tuple): The shape of the output array.
    low (int or float): The lower bound of the random values (inclusive).
    high (int or float): The upper bound of the random values (exclusive).

    Returns:
    np.ndarray: An array of random values within the specified range.
    """
    return np.random.uniform(low, high, size=shape)
random_array = random_array((3, 3), 0, 100)  # Generate a 3x3 array of random floats between 0 and 100
print("Random Array:\n", random_array)
arranged_array = np.arange(0, 100, 5)  # Create an array with values from 0 to 9
print("Arranged Array:\n", arranged_array)