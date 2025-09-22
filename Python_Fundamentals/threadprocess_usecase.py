import multiprocessing
import math
import time
import sys


sys.set_int_max_str_digits(1000000) 

# Function to calculate the factorial of a number

def calculate_factorial(number):
    """Function to calculate the factorial of a number."""
    return f"Factorial of {number} is {math.factorial(number)}"

if __name__ == "__main__":
    numbers = [5000,6000,700,8000]
    start_time = time.time()
    # Create a pool of processes
    with multiprocessing.Pool(processes=3) as pool:
        # Map the function to the numbers
        results = pool.map(calculate_factorial, numbers)
    end_time = time.time()
    # Print the results
    for result in results:
        print(result)
    print(f"Time taken: {end_time - start_time} seconds")

# This code demonstrates the use of multiprocessing to calculate the factorial of large numbers.




