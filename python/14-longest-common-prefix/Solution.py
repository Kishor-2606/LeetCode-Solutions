class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=len)
        word=strs[0]
        prefix=""
        for i in range(len(word)):
            if all(word[i]==wrd[i] for wrd in strs):
                prefix+=word[i]
            else:
                break

        return prefix
        