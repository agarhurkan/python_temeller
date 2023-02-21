import math
import time


def calculate_time(func):
    def inner(*args,**kwargs):

        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("Fonksiyon "+ func.__name__ + " " + str(finish-start)+ " saniye sürdü.")
    return inner


@calculate_time
def usalma(a,b):
    
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):

    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(3)
toplama(5,10)
