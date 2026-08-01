class Solution(object):
    def singleNumber(self, nums):
        ones=0
        twos=0
        for i in nums:
            ones=(ones^i) & ~twos
            twos=(twos^i) & ~ones
        return ones