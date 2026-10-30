class Solution:
    def isIsomorphic(self, s, t):
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # Check for mapping conflicts in s -> t
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False
            
            # Check for mapping conflicts in t -> s
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False

            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True