class Solution(object):
    def topKFrequent(self, words, k):
        freq={}
        for i in words:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        unique=list(freq.keys())
        unique.sort()
        unique.sort(key=freq.get,reverse=True)
        return unique[:k]