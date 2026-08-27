class Solution(object):
    def isNumber(self, s):
        digit,dot,e=False,False,False
        i=0
        while i<len(s):
            char=s[i]
            if char.isdigit():
                digit=True
            elif char=='+' or char=='-':
                if i>0 and s[i-1]!='e' and s[i-1]!='E':
                    return False
            elif char=='e' or char=='E':
                if e or not digit:
                    return False
                e=True
                digit=False
            elif char=='.':
                if dot or e:
                    return False
                dot=True
            else:
                return False
            i+=1
        return digit