class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        hexdigits="0123456789abcdef"
        if num<0:
            num+=2**32
        ans=[]
        while num>0:
            rem=num%16
            ans.append(hexdigits[rem])
            num//=16
        return "".join(reversed(ans))