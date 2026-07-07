class Solution(object):
    def majorityElement(self, nums):
        count=0
        num=None

        for i in nums:
            if count==0:
                num=i
            if i==num:
                count+=1
            else:
                count-=1
        return num 