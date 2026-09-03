class Solution(object):

    def mergeAlternately(self, word1, word2):
        ans = ""
        i = 0
        while i < len(word1) and i < len(word2):
            ans += word1[i]
            ans += word2[i]
            i += 1

        while i < len(word1):
            ans += word1[i]
            i += 1

        while i < len(word2):
            ans += word2[i]
            i += 1
        return ans