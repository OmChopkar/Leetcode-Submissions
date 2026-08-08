class Solution(object):
    def smallestNumber(self, n, t):
        while(True):
            num=n
            p=1
            while num>0:
                digit=num%10
                p=p*digit
                num=num//10
            if p%t==0:
                return n
            n+=1