class Solution(object):
    def frequencySort(self, nums):
        nums_dict={}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i]=1
            else:
                nums_dict[i]+=1
        
        freq_map={}
        for num,freq in nums_dict.items():
            if freq not in freq_map:
                freq_map[freq]=[]
            freq_map[freq].append(num)
        
        res=[]
        for freq in sorted(freq_map.keys()):
            num=freq_map[freq]
            num.sort(reverse=True)
        
            for val in num:
                res.extend([val] * freq)
                
        return res