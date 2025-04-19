# create processes in parallel
# When to use : CPU bound tasks , parallelism
# When not to use : IO bound tasks , multiple tasks concurrently
# Parallell processing: using all the cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(1, 6):
        print(f'Square: {i * i}')
        time.sleep(1)
def cube_numbers():
    for i in range(1, 6):
        print(f'Cube: {i * i * i}')
        time.sleep(2)

# create 2 processes
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t= time.time()

# start the processes
    p1.start()
    p2.start()

# wait for the processes to finish      
    p1.join()
    p2.join()
    completed_time = time.time()-t
    print(f"Completed in {completed_time} seconds")

