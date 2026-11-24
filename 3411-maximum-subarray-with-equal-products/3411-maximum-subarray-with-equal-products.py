class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            prod, g, l = 1, 0, 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                g = math.gcd(g, nums[j])
                l = math.lcm(l, nums[j])
                if prod == g * l:
                    ans = max(ans, j - i + 1)
        return ans