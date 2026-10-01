class Solution(object):
    def isValid(self, s):
        dic={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if i in '({[':
                stack.append(i)
            elif not stack and i in '}])':
                return False
            else:
                if stack[-1]==dic[i]:
                    stack.pop()
                else:
                    return False
        return not stack