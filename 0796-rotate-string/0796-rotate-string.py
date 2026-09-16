class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        return goal in (s+s)

        # if len(s)!=len(goal):
        #     return False
        # for _ in range(len(s)):
        #     if s==goal:
        #         return True
        #     s=s[1:]+s[0]
        # return False