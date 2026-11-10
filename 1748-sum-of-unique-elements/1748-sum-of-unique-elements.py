class Solution(object):
    def sumOfUnique(self, nums):
        nums_dict={}
        sums=0
        for i in nums:
            if i not in nums_dict:
                nums_dict[i]=1
            else:
                nums_dict[i]+=1
        for num,count in nums_dict.items():
            if count==1:
                sums+=num
        return sums