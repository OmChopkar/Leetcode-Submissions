class Solution(object):
    def containsDuplicate(self, nums):
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i,j in dict.items():
            if j>=2:
                return True
        return False