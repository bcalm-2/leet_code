def findEquilibrium(self, arr):
    # code here
    sum_right=sum(arr)
    sum_left=0
    for i in range(len(arr)):
        sum_right-=arr[i]
        if sum_right == sum_left:
            return i
        sum_left+=arr[i]
    return -1