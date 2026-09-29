class Solution(object):
    def recoverOrder(self, order, friends):
        ls=[]
        friends=set(friends)
        for i in order:
            if i in friends:
                ls.append(i)
        return ls
        