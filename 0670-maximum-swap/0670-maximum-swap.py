class Solution(object):
    def maximumSwap(self, num):
        dig=list(str(num))
        n=len(dig)
        maxnum=num
        for i in range(n):
            for j in range(i+1,n):
                dig[i],dig[j]=dig[j],dig[i]
                currnum=int(''.join(dig))
                if currnum>maxnum:
                    maxnum=currnum
                dig[i],dig[j]=dig[j],dig[i]
        return maxnum