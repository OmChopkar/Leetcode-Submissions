class Solution(object):
    def greatestLetter(self, s):
        characters=set(s)
        for i in range(25,-1,-1):
            upper = chr(65 + i)
            lower = chr(97 + i)
            if upper in characters and lower in characters:
                return upper
        return ""