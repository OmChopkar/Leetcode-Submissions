class Solution:
    def sortVowels(self, s):
        vowels = set("aeiouAEIOU")
        v = []
        for ch in s:
            if ch in vowels:
                v.append(ch)
        v.sort()

        result = []
        j = 0

        for ch in s:
            if ch in vowels:
                result.append(v[j])
                j += 1
            else:
                result.append(ch)

        return ''.join(result)