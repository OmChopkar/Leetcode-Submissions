class Solution:
    def twoSum(self, nums, target):
        dict={}
        for i in range(len(nums)):
            x=nums[i]
            val=target-x
            if val in dict:
                return[dict[val],i]
            dict[x]=i