from collections import Counter

class Solution(object):
    def totalNumbers(self, digits):
        freq = Counter(digits)
        count = 0

        for n in range(100, 1000, 2):
            d1 = n // 100
            d2 = (n // 10) % 10
            d3 = n % 10

            num_freq = Counter([d1, d2, d3])
            
            if all(freq[d] >= num_freq[d] for d in num_freq):
                count += 1
                
        return count