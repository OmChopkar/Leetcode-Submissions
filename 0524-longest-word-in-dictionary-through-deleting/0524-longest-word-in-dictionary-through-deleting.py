class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        best = ""
        for word in dictionary:
            if len(word) < len(best) or (len(word) == len(best) and word >= best):
                continue
            i = 0
            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1
            if i == len(word):
                best = word
        return best