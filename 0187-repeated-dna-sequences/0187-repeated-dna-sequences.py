class Solution:
    def findRepeatedDnaSequences(self, s):
        freq = {}

        for i in range(len(s) - 9):
            sequence = s[i:i+10]

            if sequence in freq:
                freq[sequence] += 1
            else:
                freq[sequence] = 1

        result = []

        for seq in freq:
            if freq[seq] > 1:
                result.append(seq)

        return result
