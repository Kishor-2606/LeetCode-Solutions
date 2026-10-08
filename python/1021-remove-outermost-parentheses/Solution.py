class Solution(object):
    def removeOuterParentheses(self, s):
        res=[]
        bal=0
        for c in s:
            if c=='(':
                if bal>0:
                    res.append(c)
                bal+=1
            else:
                bal-=1
                if bal>0:
                    res.append(c)
        return ''.join(res)
        