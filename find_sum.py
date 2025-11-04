# You are given an array nums of n integers and two integers k and x.

# The x-sum of an array is calculated by the following procedure:

# Count the occurrences of all elements in the array.
# Kep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
# Clculate the sum of the resulting array.
# Nte that if an array has less than x distinct elementsclass Solution(object):
def findXSum(nums, k, x):
    """
    :type nums: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    
    def x_sum(arr,x):
        if (len(list(set(arr))) < x):
            return arr
        d = {}
        for i in arr:
            d[i] = arr.count(i)
        res = []
        for i in d.keys():
            res.append([d[i],i])
        res.sort()
        res.reverse()
        f_res = []
        for i in range(x):
            for j in range(res[i][0]):
                f_res.append(res[i][1])
        return f_res
    n = len(nums)
    des = []
    for i in range(n-k+1):
        des.append(sum(x_sum(nums[i:i+k],x)))
    return des
        , its x-sum is the sum of the array.