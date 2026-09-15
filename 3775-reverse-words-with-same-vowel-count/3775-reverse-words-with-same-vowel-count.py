class Solution(object):
    def reverseWords(self, s):
        def count_vowels(word):
            count=0
            vowels={'a','e','i','o','u','A','E','I','O','U'}
            for i in word:
                if i in vowels:
                    count+=1
            return count
        words=s.split(" ")
        target=count_vowels(words[0])
        for i in range(1,len(words)):
            if count_vowels(words[i])==target:
                words[i]=words[i][::-1]
        return " ".join(words)