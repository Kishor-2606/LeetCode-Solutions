class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n, ans = len(nums), 0

        for l in range(n):
            g = lc = prod = nums[l]

            for r in range(l, n):
                if r > l:
                    g = gcd(g, nums[r])
                    lc = lcm(lc, nums[r])
                    prod *= nums[r]

                if prod == g * lc:
                    ans = max(ans, r - l + 1)

        return ans