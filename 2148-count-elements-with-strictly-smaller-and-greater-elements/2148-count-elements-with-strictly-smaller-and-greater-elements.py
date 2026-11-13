class Solution(object):
    def countElements(self, nums):
        maxNum=max(nums)
        minNum=min(nums)
        count=0
        for i in nums:
            if minNum<i<maxNum:
                count+=1
        return count