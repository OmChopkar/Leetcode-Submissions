class Solution(object):
    def checkDivisibility(self, n):
        num=n
        s,p=0,1
        while n>0:
            digit=n%10
            s+=digit
            p*=digit
            n//=10
        if num%(s+p)==0:
            return True
        return False