def moveZeroes(self, nums):
    pointer_for_zero = 0 
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[pointer_for_zero] = nums[pointer_for_zero], nums[i]
            pointer_for_zero += 1 