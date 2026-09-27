class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        is_neg = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)
        quo = 0

        while dividend >= divisor:
            temp = divisor
            mult = 1
            
            while dividend >= (temp << 1):
                temp <<= 1
                mult <<= 1

            dividend -= temp
            quo += mult
        return -quo if is_neg else quo