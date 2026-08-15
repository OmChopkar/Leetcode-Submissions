class Solution(object):
    def longestSubsequence(self, nums):
        if not any(nums):
            return 0
        xorsum=0
        for i in nums:
            xorsum^=i
        if xorsum!=0:
            return len(nums)
        else:
            return len(nums)-1