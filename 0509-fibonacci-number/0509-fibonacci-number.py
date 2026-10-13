class Solution(object):
    def fib(self, n):
        if n<=1:
            return n
        first,sec=0,1
        for i in range(2,n+1):
            first,sec=sec,first+sec
        return sec