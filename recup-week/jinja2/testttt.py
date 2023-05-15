def my_gen(num):
    while num > 0:
        yield num ** 2
        num -=1

for i in my_gen(5):
    print (i)
