import numpy as np

def sinus_generator(amplitudo, frekuensi, t_akhir, theta):
    t= np.arange(0, t_akhir, 0.1)
    y= amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))

    return t, y

# sinus_generator example: t, y= sinus_generator(1,1,4,0)

def random_generator(size=20):
    a = np.random.randint(30, 50, size=size)

    return a

# random_generator example: a= random_generator(10)

def consecutive_generator(size=20, iteration= 1, start=0):
    # arr= [i for i in range(0, size, iteration)]
    arr= []
    i= start
    temp_size= 0

    while temp_size<size:
        arr.append(i)

        i+=iteration
        temp_size+= 1

    return arr

# consecutive generator example: c= consecutive_generator2(10, 0.5)

def consecutive_generator2(size=20, start=0, end=None):
    if end is None:
        end = size + start

    i = start
    iteration= (end-start)/size

    arr = []
    temp_size = 0

    while temp_size < size:
        arr.append(i)

        i += iteration
        temp_size += 1

    return arr

# consecutive generator2 example: c= consecutive_generator2(10, start=2, end=20)