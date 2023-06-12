import time
from random import randint



def performance_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to run.")
        return result
    return wrapper



@performance_decorator
def merge1(nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()


@performance_decorator
def merge2(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    k = n + m - 1
    m = m - 1 
    n = n - 1  
    # we need last indexes to do the job
    # first perform merge
    while m >= 0 and n >= 0:
        if nums1[m] >= nums2[n]:
            nums1[k], nums1[m] = nums1[m], nums1[k]
            k -= 1
            m -= 1
        else:
            nums1[k] = nums2[n]
            k -= 1
            n -= 1
    # get ther rest of values is nums2 has any..
            
    while n >= 0:
        nums1[k] = nums2[n]
        k -= 1
        n -= 1
    # and we don't need to add rest of nums1 as it is already inplace  and 
    

n = 20000000
m = 20000000
numss2 = []
nums1 = []
nums2 = []
nums3 = []
nums4 = []
nums5 = []
nums6 = []
nums7 = []
nums8 = []
nums9 = []
s = 1
for i in range(m):
    s += randint(1,10)
    nums1.append(s)
    nums2.append(s)
    nums3.append(s)
    nums4.append(s)
    nums5.append(s)
    nums6.append(s)
    nums7.append(s)
    nums8.append(s)
    nums9.append(s)
     
s = 0
for i in range(n):
    s += randint(1,10)
    numss2.append(s)
    
    nums1.append(0)
    nums2.append(0)
    nums3.append(0)
    nums4.append(0)
    nums5.append(0)
    nums6.append(0)
    nums7.append(0)
    nums8.append(0)
    nums9.append(0)

nums_to_sort = nums1.copy

flag = input()

while flag !="x":
    
    
    merge1(nums1, m, numss2, n)
    
    nums_to_sort = nums1.copy()

    merge2(nums2, m, numss2, n)

    flag = input()

    merge1(nums3, m, numss2, n)
    
    nums_to_sort = nums1.copy()

    merge2(nums4, m, numss2, n)

    flag = input()

    merge1(nums5, m, numss2, n)
    
    nums_to_sort = nums1.copy()

    merge2(nums6, m, numss2, n)

    flag = input()

    merge1(nums7, m, numss2, n)
    
    nums_to_sort = nums1.copy()

    merge2(nums8, m, numss2, n)

    flag = input()

   