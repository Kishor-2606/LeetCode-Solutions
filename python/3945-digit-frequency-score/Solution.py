class Solution(object):
    def digitFrequencyScore(self, n):
        score=0
        freq={}
        digit=0
        while(n!=0):
            digit=n%10
            n=n/10
            freq[digit]=freq.get(digit,0)+1
        for key,value in freq.items():
            score+=key*value
        return score
