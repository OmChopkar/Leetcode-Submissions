class Solution(object):
    def maxFreqSum(self, s):
        vowel={}
        consonant={}
        for i in s:
            if i.isalpha():
                if i in "aeiou":
                    if i not in vowel:
                        vowel[i]=1
                    else:
                        vowel[i]+=1
        for i in s:
            if i.isalpha():
                if i not in "aeiou":
                    if i not in consonant:
                        consonant[i]=1
                    else:
                        consonant[i]+=1
        max_vowel=max(vowel.values()) if vowel else 0
        max_consonant=max(consonant.values()) if consonant else 0

        return max_vowel+max_consonant