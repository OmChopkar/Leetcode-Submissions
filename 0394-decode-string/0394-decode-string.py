class Solution(object):
    def decodeString(self, s):
        numStack=[]
        strStack=[]
        current=""
        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=="[":
                numStack.append(num)
                strStack.append(current)
                num=0
                current=""
            elif i.isalpha():
                current+=i
            elif i=="]":
                repeat=numStack.pop()
                previous=strStack.pop()
                current=previous+current*repeat
        return current