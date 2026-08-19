class Solution(object):
    def mergeAlternately(self, word1, word2):
        new=[]
        i,j=0,0

        while i<len(word1) and j<len(word2):
            new.append(word1[i])
            new.append(word2[j])
            i+=1
            j+=1
        
        if i<len(word1):
            new.append(word1[i:])
        
        if j<len(word2):
            new.append(word2[j:])

        return "".join(new)