import multiprocessing
"""
CPUs have different number of processors i.e.the number of cores in your CPU.
All the programs not using multiprocessing will be allocated only a single core
to work with. So at a time you will only be using a fraction of what your whole
CPU is capable of. Say, you have a quad core processor, meaning a normal program
will be using just 25% of your CPUs capability.
Using multiprocessing, you can divide the work among all your cores and use a
larger fraction of your CPUs capability.
In the below example we want to call a function named spawn() 10 times, which should
take 10 times the time of a single call. But by using multiprocessing, we divide
the work among our cores and get the work done in lesser time.
We can actually look at the multiple process running using task manager.
"""
#Everything that you want to multiprocess needs to be put inside a fuction and then
#called through the target parameter of a Process() of a multiprocessing object.

def spawn(num):         
    print("Spawned {}".format(num))

if __name__ == '__main__':      #Doing this is important for multiprocessing
    for i in range(10):
        p = multiprocessing.Process(target=spawn, args=(i,))    `,
        #A trailing ',' is required if there is only a single argument
        p.start()               #Starts the multiprocessing
        p.join()
        #join() waits for one process to get finished before calling the next
        #process. Without it, the processes will not wait for each other.


"""
HOW TO USE
1. Open cmd prompt and nevigate to the folder where the file is kept.
2. Run the program using 'py filename.py'
"""

"""
OUTPUT in the command prompt will look like:
#With join

C:\MvikBack\Python\ToUpload\Intermediate python>py Multiprocessing.py
Spawned 0
Spawned 1
Spawned 2
Spawned 3
Spawned 4
Spawned 5
Spawned 6
Spawned 7
Spawned 8
Spawned 9


#Without join

C:\MvikBack\Python\ToUpload\Intermediate python>py Multiprocessing.py
Spawned 1
Spawned 2
Spawned 4
Spawned 0
Spawned 7
Spawned 9
Spawned 3
Spawned 6
Spawned 5
Spawned 8
"""
