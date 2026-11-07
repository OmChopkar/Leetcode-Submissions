class Solution:
    def frequencySort(self, s):
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        def get_count(item):
            return item[1]

        sorted_chars = sorted(counts.items(), key=get_count, reverse=True)

        result = []
        for char, freq in sorted_chars:
            result.append(char * freq)
            
        return "".join(result)