class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        t=len(nums)//3
        res=[]
        for i,j in count.items():
            if j>t:
                res.append(i)
        return res