class Solution(object):
    def reverseDegree(self, s):
        totalsum=0
        for i in range(len(s)):
            ch=s[i]
            pos=i+1
            rev_pos=26-(ord(ch)-ord('a'))
            totalsum+=pos*rev_pos
        return totalsum