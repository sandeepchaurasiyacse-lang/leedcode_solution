class Solution(object):

    def checkDivisibility(self, n):

        digit_sum = 0
        digit_product = 1

        for i in str(n):
            digit = int(i)
            digit_sum += digit
            digit_product *= digit

        if n % (digit_sum + digit_product) == 0:
            return True
        else:
            return False