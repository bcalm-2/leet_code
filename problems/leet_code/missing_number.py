def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums) + 1
    for num in range(0, n):
        if num not in nums:
            return num
                
print(missingNumber([9,6,4,2,3,5,7,0,1] ))
print(missingNumber([1, 0]))