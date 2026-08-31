class Solution(object):
    def findNonMinOrMax(self, nums):
        minnum=min(nums)
        maxnum=max(nums)
        for i in nums:
            if i!=minnum and i!=maxnum:
                return i
        return -1