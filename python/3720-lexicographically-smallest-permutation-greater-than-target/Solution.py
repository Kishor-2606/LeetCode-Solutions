class Solution(object):
    def lexGreaterPermutation(self, s, target):
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        n=len(s)
        for i in range(n-1,-1,-1):
            freq2=freq.copy()
            for j in range(i):
                ch=target[j]

                if freq2.get(ch,0)==0:
                    break
                freq2[ch]-=1
            else:
                for ch in sorted(freq2):
                    if ch>target[i] and freq2[ch]>0:
                        freq2[ch]-=1
                        ans=target[:i]+ch
                        for c in sorted(freq2):
                            ans+=c*freq2[c]
                        return ans
        return ""