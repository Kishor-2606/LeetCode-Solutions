class Solution(object):
    def decrypt(self, code, k):
        if k<0:
            window_sum=sum(code[k:])
        else:
            window_sum=sum(code[1:k+1])
        ls=[]
        ls.append(window_sum)
        val=0
        for i in range(1,len(code)):
            if k<0:
                val=i+k-1
                window_sum=window_sum+code[i-1]-code[val]
            else:
                val=(i+k)%len(code)
                window_sum=window_sum-code[i]+code[val]
            ls.append(window_sum)
        return ls