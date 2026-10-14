class Solution(object):
    def maxSumOfSquares(self, num, sm):
        digit=9
        ls=""
        copy=sm
        num_c=num
        spy=0
        while(copy!=0 and num!=0):
            if copy>=digit:
                copy-=digit
                ls+=str(digit)
                spy+=digit
                num-=1
            else: digit-=1

        if sm>spy:return ""
        
        if len(ls)<num_c:
            zer=num_c-len(ls)
            ls+="".join(["0"]*zer)
        return ls

            
        