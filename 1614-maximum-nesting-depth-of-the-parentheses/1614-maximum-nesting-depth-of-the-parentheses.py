class Solution(object):
    def maxDepth(self, s):
        maxDepth=0
        current=0
        for i in s:
            if i=='(':
                current+=1
                maxDepth=max(maxDepth,current)
            elif i==')':
                current-=1
        return maxDepth