class Solution(object):
    def finalPrices(self, prices):
        n = len(prices)
        stack = []
        discounts = [0] * n
        discounts[n - 1] = prices[n - 1]
        stack.append(prices[n - 1])

        for i in range(n - 2, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()

            if stack:
                discounts[i] = prices[i] - stack[-1]
            else:
                discounts[i] = prices[i]

            stack.append(prices[i])

        return discounts
        