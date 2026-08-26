class Solution(object):

    def lengthOfLongestSubstring(self, s):

        longest = 0
        sub = ""
        for ch in s:
            if ch in sub:
                sub = sub[sub.index(ch) + 1:]
            sub = sub + ch
            if len(sub) > longest:
                longest = len(sub)
        return longest