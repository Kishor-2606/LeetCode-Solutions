class Solution(object):
    def mirrorFrequency(self, s):
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        k=0
        m=0
        for i in s:
            if i>='a' and i<='z':
                k=chr((97) + (25-(ord(i)-97)))
                m=m+abs(freq.get(i,0)-freq.get(k,0))
                
            elif i>='A' and i<='Z':
                k=chr((65) + (25-(ord(i)-65)))
                m=m+abs(freq.get(i,0)-freq.get(k,0))
                
            else:
                k=chr((48) + (9-(ord(i)-48)))
                m=m+abs(freq.get(i,0)-freq.get(k,0))

            freq.pop(i,None)
            freq.pop(k,None)

        return m