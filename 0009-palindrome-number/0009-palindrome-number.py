class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        n = x
        rev = 0
        while n > 0:
            last_digit = n % 10
            rev = rev * 10 + last_digit
            n = n // 10
        if x == rev:
            return True
        else:
            return False