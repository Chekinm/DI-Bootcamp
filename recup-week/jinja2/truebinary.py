def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    N = len(nums)
    # as array is sorted  can use binary serach here    
    #find left edge of target subarray
    ll = -1
    lr = N
    while lr - ll > 1:
        m = ll + ((lr-ll) // 2)
        if nums[m] < target:
            ll=m
        elif nums[m] >= target:
            lr=m
    # target supposingly start at lr (left_right) 
    #find right edge
    rl = -1
    rr = N
    while rr - rl > 1:
        m = rl + (rr -rl) // 2
        if nums[m] <= target:
            rl=m
        elif nums[m] > target:
            rr=m
    # target supposingly ends at rl (right_left) 
    # check if target exist in array
    print(ll,lr,rl, rr)
    return [lr,rl] if rr - ll > 1 else [-1,-1]

print(searchRange([1,2], 0))