class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a=[]
        def helper(s,o,c):
            if c<o or o<0 or c<0:
                return
            if len(s)==2*n:
                a.append(s)
            helper(s+"(",o-1,c)
            helper(s+")",o,c-1)
        helper("",n,n)
        return a
            