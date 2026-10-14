class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        note={}
        for i in ransomNote:
            if i in note:
                note[i]+=1
            else:
                note[i]=1
        
        mag={}
        for i in magazine:
            if i in mag:
                mag[i]+=1
            else:
                mag[i]=1
        
        for i in note:
            if i not in mag or mag[i]<note[i]:
                return False
        return True