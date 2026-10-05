class Solution(object):
    def scoreOfParentheses(self, s):
        stack = [0]
        for ch in s:
            if ch=='(':
                stack.append(0)
            else:
                inside=stack.pop()
                if inside==0:
                    stack.append(stack.pop()+1)
                else:
                    stack.append(stack.pop()+2*inside)
        return stack.pop()
        