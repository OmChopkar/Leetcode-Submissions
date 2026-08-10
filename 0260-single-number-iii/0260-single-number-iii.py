class Solution(object):
    def singleNumber(self, nums):
        dict={}
        L=[]
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i,j in dict.items():
            if j==1:
                L.append(i)
        return L