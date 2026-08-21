class Solution(object):
    def findGCD(self, nums):
        min_nums=min(nums)
        max_nums=max(nums)
        a,b=min_nums,max_nums
        while b!=0:
            a,b=b,a%b
        return a