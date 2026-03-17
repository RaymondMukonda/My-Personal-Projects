from multiprocessing import Process, Value, Array, Lock
import os

def square_number():
    for i in range(1000):
        i * i 

if __name__ == "__main__":
    processes = []
    num_prcesses = os.cpu_count()
    # number of CPUs on the machine. Usally good choice for number of processes

    # create processes and asign a function for each process
    for i in range(num_prcesses):
        process = Process(target=square_number)
        processes.append(process)

    # strt all processes
    for process in  processes:
        process.start()

    # wait till all processes to finish 
    # block the main program until these processes are finished 
    for processs in processes:
        process.join()

#################################################################

import time

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock: # this does the same as lock acquire and lock release
            number.value += 1


if __name__ == "__main__":

    lock = Lock()
    shared_number = Value("i", 0)
    print("Number at the beginning is", shared_number.value)

    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))


    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Number  at end is", shared_number.value)