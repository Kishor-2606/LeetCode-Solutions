class Solution(object):
    def maximumWealth(self, accounts):
        mx=float('-inf')
        for i in accounts:
            sm=0
            for j in i:
                sm+=j
            mx=max(mx,sm)
        return mx