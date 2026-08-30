class Solution(object):
    def getHint(self, secret, guess):
        cnt=0
        cnt2=0
        i=0
        freq1={}
        freq2={}
        while i<len(secret):
            if secret[i]==guess[i]:
                cnt+=1
            else:
                freq1[secret[i]]=freq1.get(secret[i],0)+1
                freq2[guess[i]]=freq2.get(guess[i],0)+1
            i=i+1
        for key,value in freq1.items():
            cnt2+=min(value,freq2.get(key,0))

        return str(cnt)+"A"+str(cnt2)+"B"
        

        