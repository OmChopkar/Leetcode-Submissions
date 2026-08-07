class Solution(object):
    def singleNonDuplicate(self, nums):
        ans=0
        for i in nums:
            ans^=i        
        return ans