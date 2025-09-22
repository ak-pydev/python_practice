### Multithreading with ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    """Function to print a number with a delay."""
    time.sleep(1)  # Simulate a delay
    return f"Number printed: {number}"

number = [1,2,3,4,5,6,7,8,9,10]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, number)

for result in results:
    print(result)  

## Multithreading with ThreadPoolExecutor and Future
from concurrent.futures import ProcessPoolExecutor
import time

def print_square(number):
    """Function to print the square of a number with a delay."""
    time.sleep(1)  # Simulate a delay
    return f"Square printed: {number * number}"
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results2 = executor.map(print_square, number)

    for result in results2:
        print(result)