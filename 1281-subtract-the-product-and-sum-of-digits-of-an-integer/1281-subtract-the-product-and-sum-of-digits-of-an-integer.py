class Solution(object):
    def subtractProductAndSum(self, n):
        summ=0
        prod=1
        while n>0:
            digit=n%10
            summ+=digit
            prod*=digit
            n=n//10
        return prod-summ