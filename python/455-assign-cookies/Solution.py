
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i=0
        j=0
        while(True):
            if len(g)<=i or len(s)<=j:
                    break
            elif g[i]<=s[j]:
                i+=1
                j+=1 
            else:
                j+=1
        return i

            
        