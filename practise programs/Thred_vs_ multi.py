# Threading vs Multiprocessing 
#  Process: An instance of a program  (e.g a Python interpreter)

#  + Takes advantage of multiple CPUs  and cores 
#  + Separate memory space -> Memory is not shared between prrocesses
#  + Great for CPU-bound processing 
#  + New process is stated independently from other processes
#  + Processes are interruptable/ killable 
#  + One GIL for each process -> avids GIL limitation

#  -  Heavyweight
#  - Starting a proceess is slower then starting a thread 
#  - More memory 
#  - IPC  ( inter-process communication) is more comaplicated 