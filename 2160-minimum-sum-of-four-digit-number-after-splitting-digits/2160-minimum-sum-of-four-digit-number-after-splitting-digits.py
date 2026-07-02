class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        ls=[]
        dub=num
        while(dub!=0):
            ls.append(str(dub%10))
            dub=dub//10
        ls.sort()
        n1=int(ls[0]+ls[3])
        n2=int(ls[1]+ls[2])
        n3=n1+n2
        return n3

