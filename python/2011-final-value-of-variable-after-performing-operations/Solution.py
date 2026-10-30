class Solution(object):
    def finalValueAfterOperations(self, operations):
        x=0
        for i in operations:
            if i=='--X' or i=='X--':
                x=x-1
            else: x=x+1
        return x