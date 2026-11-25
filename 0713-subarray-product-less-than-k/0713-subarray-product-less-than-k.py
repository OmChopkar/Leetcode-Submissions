class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if k<=1:
            return 0
        count=0
        prod=1
        left=0
        for right in range(n):
            prod*=nums[right]
            while prod>=k:
                prod//=nums[left]
                left+=1
            count+=right-left+1
        return count