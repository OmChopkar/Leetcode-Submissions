class Solution(object):
    def moveZeroes(self, nums):
        nonZero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[nonZero],nums[i]=nums[i],nums[nonZero]
                nonZero+=1