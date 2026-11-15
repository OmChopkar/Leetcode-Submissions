class Solution(object):
    def numOfSubarrays(self, arr):
        MOD=10**9+7
        odd=0
        even=1
        pre=0
        count=0
        for i in arr:
            pre+=i
            if pre%2==0:
                count+=odd
                even+=1
            else:
                count+=even
                odd+=1
        return count%MOD