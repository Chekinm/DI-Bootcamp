from functools import reduce
from operator import mul
def fact(n):
    return reduce(mul, iter(range(1,n)))

print(fact(10))



