class Solution(object):
    def arrangeCoins(self, n):
        start=1
        end=n
        answer=1
        while start<=end:
            middle=(start+end)//2
            print(middle)
            coins=middle*(middle+1)//2
            print(coins)
            print(start,end)
            if coins>n:
                end=middle-1
            elif coins<=n:
                answer=middle
                start=middle+1
            print(answer)
        return answer