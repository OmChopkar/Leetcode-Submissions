class Solution(object):
    def firstMissingPositive(self, nums):
        num_set=set(nums)
        ans=1
        while ans in num_set:
            ans+=1
        return ans 