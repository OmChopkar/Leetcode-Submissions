class Solution(object):
    def firstUniqChar(self, s):
        dict={}
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i in range(len(s)):
            letter=s[i]
            if dict[letter]==1:
                return i
        return -1