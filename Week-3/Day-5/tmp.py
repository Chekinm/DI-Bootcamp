# from time import time
# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper

# @performance
# def long_time():
#     print('1')
#     for i in range(10000000):
#         i*5
# @performance
# def new_list(a):
#     a = list(range(10000000))
#     return a

# a=[]

# a = new_list(a)



# @performance
# def long_time2():
#     print('2')
#     for i in a:
#         i*5




# long_time()
# long_time2()

def create_key(word):
    return ''.join(sorted(set(word.lower())))

print(create_key('Meat'))
