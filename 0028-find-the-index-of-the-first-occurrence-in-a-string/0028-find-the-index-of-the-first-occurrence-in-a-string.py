class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if needle not in haystack:
                return -1
            else:
                fin=haystack.find(needle)
        return fin