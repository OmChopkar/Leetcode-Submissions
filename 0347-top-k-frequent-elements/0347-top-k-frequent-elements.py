class Solution(object):
    def topKFrequent(self, nums, k):
        eleCount={}
        res=[]

        for i in nums:
            if i in eleCount:
                eleCount[i]+=1
            else:
                eleCount[i]=1
        
        sorted_eleCount=sorted(eleCount,key=eleCount.get,reverse=True)

        return sorted_eleCount[:k]