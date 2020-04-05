#Onjective to get return values from multiprocessing to our script.

from multiprocessing import Pool

#Our process that need to be completed.
def job(num):
    return num * 2

if __name__ == '__main__':
    #Below line describes that we have 20 different workers that will do our job
    p = Pool(processes=20)
    #Below line describes that the 30 jobs needs to be done.
    data = p.map(job, range(30))  #We map the job to some iterable eg :generator
    data2 = p.map(job, [3, 4, 2])
    p.close()
    print(data)
    print(data2)

"""
OUTPUT

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
40, 42, 44, 46, 48, 50, 52, 54, 56, 58]
[6, 8, 4]

"""
