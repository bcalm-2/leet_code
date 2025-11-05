def getSecondLargest(self, arr):
    # Code Here
    largest = -1
    second_largest = -1
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and not num == largest:
            second_largest = num
    return second_largest