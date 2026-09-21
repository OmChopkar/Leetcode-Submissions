class Solution(object):
    def largestNumber(self, nums):
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        n=len(nums)
        
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j] + nums [j+1] < nums[j+1] + nums[j]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        result=""
        for i in range(n):
            result+=nums[i]
        if result[0]=="0":
            return "0"
        return result