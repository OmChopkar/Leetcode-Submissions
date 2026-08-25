class Solution(object):
    def missingMultiple(self, nums, k):
        numset=set(nums)
        mult=k
        while mult in numset:
            mult+=k
        return mult