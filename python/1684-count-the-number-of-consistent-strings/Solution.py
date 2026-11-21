class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0

        for word in words:
            if all(char in allowed for char in word):
                count += 1

        return count
            