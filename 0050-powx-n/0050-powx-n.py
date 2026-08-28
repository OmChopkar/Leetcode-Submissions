class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn = abs(n)
        res = 1.0
        
        while nn > 0:
            if nn % 2 == 1:
                res *= x

            x *= x
            nn //= 2
            
        return res if n >= 0 else 1.0 / res

        