class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words=re.findall(r"[a-z]+",paragraph.lower())
        banned_words=set()
        for word in banned:
            banned_words.add(word.lower())
        freq={}
        for word in words:
            if word not in banned_words:
                if word in freq:
                    freq[word]+=1
                else:
                    freq[word]=1
        maxfreq=0
        bestword=""
        for word,count in freq.items():
            if count>maxfreq:
                maxfreq=count
                bestword=word
        return bestword