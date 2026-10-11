class Solution(object):
    def sumOfSquares(self, nums):
        n=len(nums)
        sqSum=0
        for i in range(1,n+1):
            if n%i==0:
                sqSum+=nums[i-1]**2
        return sqSum