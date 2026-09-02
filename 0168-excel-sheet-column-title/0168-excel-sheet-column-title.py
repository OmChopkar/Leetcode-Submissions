class Solution(object):
    def convertToTitle(self, columnNumber):
        ans=[]
        while columnNumber>0:
            columnNumber-=1
            rem=columnNumber%26
            ans.append(chr(65+rem))
            columnNumber//=26
        return ''.join(reversed(ans))