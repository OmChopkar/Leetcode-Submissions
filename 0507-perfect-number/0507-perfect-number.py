class Solution(object):
    def checkPerfectNumber(self, num):
        if num<=1:
            return False
        div_sum=1
        i=2
        while i*i<=num:
            if num%i==0:
                div_sum+=i
                if i!=num//i:
                    div_sum+=num//i
            i+=1
        return div_sum==num