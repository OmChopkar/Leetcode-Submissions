class Solution(object):
    def majorityFrequencyGroup(self, s):
        s_dict={}
        for i in s:
            if i not in s_dict:
                s_dict[i]=1
            else:
                s_dict[i]+=1
        
        freq_dict = {}
        for i, j in s_dict.items():
            if j not in freq_dict:
                freq_dict[j] = [i]
            else:
                freq_dict[j].append(i)

        max_size=0
        max_freq=0
        for i, j in freq_dict.items():
            if len(j) > max_size or (len(j) == max_size and i > max_freq):
                max_size = len(j)
                max_freq = i

        return ''.join(freq_dict[max_freq])