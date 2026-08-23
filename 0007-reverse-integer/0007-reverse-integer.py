class Solution(object):
    def reverse(self, x):
        rev = 0
        mark = 1
        if x < 0:
            mark = -1
            x = -x
        while x > 0:
            last_digit = x % 10
            rev = rev * 10 + last_digit
            x = x // 10
        rev = rev * mark
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev