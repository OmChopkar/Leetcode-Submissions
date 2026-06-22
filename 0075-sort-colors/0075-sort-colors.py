class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            min=i
            j=i+1
            while j<len(nums):
                if nums[j]<nums[min]:
                    min=j
                j+=1
            temp=nums[i]
            nums[i]=nums[min]
            nums[min]=temp
          
