class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        if k<=0 or k>n:
            return None
        window_sum=sum(nums[:k])
        max_sum=window_sum
        for right in range(k,n):
            window_sum+=nums[right]-nums[right-k]
            max_sum=max(max_sum,window_sum)
        return max_sum/float(k)