class Solution(object):
    def findWords(self, words):
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")
        
        result=[]

        for i in words:
            word=set(i.lower())
            if word.issubset(row1) or word.issubset(row2) or word.issubset(row3):
                result.append(i) 
        
        return result