class Solution(object):
    def maxSumOfSquares(self, num, sm):

        digit=9
        ls=[]
        copy=sm
        num_c=num
        while(copy!=0):
            if copy>=digit:
                copy-=digit
                ls.append(digit)
                num-=1
            else:
                digit-=1
            if num==0:
                break

        if sm>sum(ls):
            return ""
        else:
            if len(ls)<num_c:
                zer=num_c-len(ls)
                ls.extend([0]*zer)
            return "".join([str(i) for i in ls])

            
        