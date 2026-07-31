class Solution(object):
    def minimumPushes(self, word):
        freq=[0]*26
        for ch in word:
            freq[ord(ch)-ord('a')]+=1
        freq.sort()
        cnt=0
        ans=0
        for f in reversed(freq):
            if f>0:
                cnt+=1
            if cnt<=8:
                ans+=f
            elif cnt<=16:
                ans+=f*2
            elif cnt<=24:
                ans+=f*3
            else:
                ans+=f*4
        return ans
        