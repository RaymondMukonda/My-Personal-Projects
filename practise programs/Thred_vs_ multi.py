# Threading vs Multiprocessing 

#  Process: An instance of a program  (e.g a Python interpreter)

#  + Takes advantage of multiple CPUs  and cores 
#  + Separate memory space -> Memory is not shared between prrocesses
#  + Great for CPU-bound processing 
#  + New process is started independently from other processes
#  + Processes are interruptable/ killable 
#  + One GIL for each process -> avids GIL limitation

#  -  Heavyweight
#  - Starting a proceess is slower then starting a thread 
#  - More memory 
#  - IPC  ( inter-process communication) is more comaplicated 

#  Threads: An entity within a process that can be scheduled (also known as "Leightweight process"
#  A process can spwan multiple threads.

#  +  All threads witnin a process share the same memory 
#  + leightweight 
#  + starting a thread is faster then starting a process
#  + Great for I/O- bound tasks [ input ouput tasks]

#  - Thread is limited to GIL: Only one thread at a time 
#  - No effects for CPU-bound tasks 
#  - Not interruptable/ killable
#  - Careful with race conditions 

# Gil: Global interpreter lock 

#  - A lock that allows only one thread at a time to execute in python 
#  - Needed in CPython becuase memory management is not thread-safe 

#  -Avoid:
#  - Use multiprocessing 
#  - Use a different,  free-threaded Pyhton implementation (Jython, IronPython)
#  - Use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy

 