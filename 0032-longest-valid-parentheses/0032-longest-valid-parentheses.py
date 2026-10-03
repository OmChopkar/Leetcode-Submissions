class Solution(object):
    def longestValidParentheses(self, s):
        stack=[-1]
        max_len=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    current_len=i-stack[-1]
                    if current_len>max_len:
                        max_len=current_len
        return max_len