class Solution(object):
    def findNumbers(self, nums):
        total=0
        for i in nums:
            digit=0
            while i>0:
                i//=10
                digit+=1
            
            if digit%2==0:
                total+=1
        return total

        # total=0
        # for i in nums:
        #     if len(str(i))%2==0:
        #         total+=1
        # return total
