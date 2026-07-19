class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        stack=[]
        stack.append(s[0])
        dic[s[0]]-=1
        # print(stack)
        for i in s[1:]:
            dic[i]-=1
            if i in stack:
                continue
            elif stack[-1]>i:
                while(True):
                    if len(stack)==0:
                        break
                    elif stack[-1]>i and dic[stack[-1]]>=1:
                        stack.pop()
                    else:
                        break
            stack.append(i)
        return "".join(stack)
        

            