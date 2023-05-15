from functools import reduce

a = [1,2,3,4]

b= reduce(lambda x, y: x* y, a)
print(b)