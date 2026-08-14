class Solution(object):
    def findDisappearedNumbers(self, nums):
        set_nums=set(nums)
        result=[]
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                result.append(i)
        return result