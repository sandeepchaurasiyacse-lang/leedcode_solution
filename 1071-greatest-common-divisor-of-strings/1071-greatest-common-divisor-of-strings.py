class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        a = len(str1)
        b = len(str2)
        while b != 0:
            temp = b
            b = a % b
            a = temp

        return str1[:a]