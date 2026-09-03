class Solution(object):
    def titleToNumber(self, columnTitle):
        ans=0
        for i in columnTitle:
            val=ord(i)-ord('A')+1
            ans=ans*26+val
        return ans