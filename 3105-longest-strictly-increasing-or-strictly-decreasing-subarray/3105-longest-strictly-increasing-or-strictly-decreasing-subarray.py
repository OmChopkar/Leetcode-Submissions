class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc=dec=maxLength=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                inc+=1
                dec=1
            elif nums[i] < nums[i-1]:
                dec+=1
                inc=1
            else:
                inc=1
                dec=1
            maxLength = max(maxLength, inc, dec)
        return maxLength