class Solution(object):
    def addDigits(self, num):
        if num==0:
            return 0
        while num>=10:
            sums=0
            while num>0:
                digit=num%10
                sums+=digit
                num//=10
            num=sums
        return num