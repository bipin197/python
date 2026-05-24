import numpy as np
random_array = np.random.randint(0, 100, (3, 3), dtype=np.int16)  # Generate a 3x3 array of random integers
print("Random Array:\n", random_array)
# Calculate the mean of the random array
mean_value = np.mean(random_array)
print("Mean Value:", mean_value)
# Calculate the standard deviation of the random array
std_dev_value = np.std(random_array)
print("Standard Deviation:", std_dev_value) 