class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        nums_dict={}
        res=[]
        for i in nums:
            if i in nums_dict:
                nums_dict[i]+=1
            else:
                nums_dict[i]=1
        for i,freq in nums_dict.items():
            if freq>=2:
                res.append(i)
        return res