class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            n=nums[i]
            digitSum=0
            while n>0:
                digitSum+=n%10
                n//=10

            if digitSum==i:
                return i
        return -1