class Solution(object):

    def kidsWithCandies(self, candies, extraCandies):
        result = []
        greatest = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)

        return result