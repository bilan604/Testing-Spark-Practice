from random import randint
from timeit import default_timer

n = 10**6


start = default_timer()
inp = [randint(0,15) for itr in range(n)]
stop = default_timer()

print(stop-start)








