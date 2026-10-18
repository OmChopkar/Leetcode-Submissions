class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1==s2:
            return True
        
        diffIndex=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diffIndex.append(i)
        
        if len(diffIndex)==2:
            i,j=diffIndex
            return s1[i]==s2[j] and s1[j]==s2[i]
        
        return False