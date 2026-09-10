class Solution(object):
    def vowelConsonantScore(self, s):
        c=v=0
        for i in s:
            if i.isalpha():
                if i in "aeiou":
                    v+=1
                else:
                    c+=1
        return v//c if c>0 else 0 