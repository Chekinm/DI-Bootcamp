def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    def bin_search(nums, l, r, target):               # [1,3,5,6,7], target = 2 r = 
        if r-l == 1:
            return l if nums[l] == target else l + 1           #r- l = 2    zero case FIXIT 
        else:
            mid = l + (r - l) // 2                           #  2               
            if nums[mid] > target:
                return bin_search (nums, l, mid, target)  #  (num, 0,2, 2)
            elif nums[mid] < target: 
                return bin_search (nums, mid, r, target)
            else:
                return mid

    l = 0
    r = len(nums)
    return bin_search(nums, l, r, target)

print(searchInsert([1,2,3,5,7,8,9,12,14],11))



SELECT name AS Employee 
FROM (SELECT name AS name, salary AS s, managerid AS m 
      FROM Employee 
      WHERE managerId IS NOT NULL) tbl
WHERE s > (SELECT salary 
          FROM Employee 
          WHERE id = m) 