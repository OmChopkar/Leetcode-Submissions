class Solution(object):
    def findPeakElement(self, nums):
        max_num=max(nums)
        return nums.index(max_num)