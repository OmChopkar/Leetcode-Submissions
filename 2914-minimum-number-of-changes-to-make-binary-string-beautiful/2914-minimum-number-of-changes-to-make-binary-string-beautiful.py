class Solution(object):
    def minChanges(self, s):
        flip=0
        for i in range(0,len(s),2):
            if s[i]!=s[i+1]:
                flip+=1
        return flip
