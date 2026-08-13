class Solution(object):
    def findTheDifference(self, s, t):
        new=s+t
        ans=0
        for i in new:
            ans^=ord(i)
        return chr(ans)