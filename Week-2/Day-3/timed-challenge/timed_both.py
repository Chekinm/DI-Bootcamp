# reverse phrase

a = 'hwllo sdf  werwe  qqqq'

list = a.split()

list2 = []
while list:
    list2.append(list.pop())

print(' '.join(list2))


# is perfect

def is_perfect(num):
    i = 2
    sum_dev = 1
    while i <= num/2:
        if num % i == 0:
            sum_dev += i
        i += 1

    return True if  sum_dev == num else False
    

print(is_perfect(33550336))


for i in range(10000):
    if is_perfect(i):
        print(i)