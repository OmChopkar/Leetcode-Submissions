class Solution(object):
    def singleNumber(self, nums):
        unique=0
        for i in nums:
            unique=unique^i
        return unique