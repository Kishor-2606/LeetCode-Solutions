class Solution(object):
    def checkString(self, s):
        flag=True
        for i in s:
            if i =='a' and flag:
                continue
            elif i=='b':
                flag=False
            else:
                return False
        return True