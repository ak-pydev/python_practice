## Multithreading 

# When to use : IO bound tasks , multiple tasks concurrently
# When not to use : CPU bound tasks , parallelism

import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(0.2) 
         
def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(0.2)
#create 2 threads 

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t= time.time()

#start the threads
t1.start()  
t2.start()

#wait for the threads to finish
t1.join()
t2.join() 

print_letters()
print_numbers()
completed_time = time.time()-t
print(f"Completed in {completed_time} seconds")
