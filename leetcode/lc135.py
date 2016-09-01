class Solution(object):
    @staticmethod
    def _candies(ratings):
        candies = [0] * len(ratings)

        is_start = True
        candies[0] = 1
        for i in range(1, len(candies)):
            current = ratings[i]
            last = ratings[i-1]
            if current > last:
                candies[i] = candies[i-1] + 1
            # elif current == last:  # XXX That is what they want
                # candies[i] = candies[i-1]
            else:  # current < last
                candies[i] = 1
        for i in range(len(candies) - 1 - 1, -1, -1):
            current = ratings[i]
            last = ratings[i+1]
            if current > last:
                suggest_value = candies[i+1] + 1
            # elif current == last:  # XXX That is what they want
                # suggest_value = candies[i+1]
            else:
                suggest_value = 1
            if suggest_value > candies[i]:
                candies[i] = suggest_value
        
        return candies


    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        return sum(self._candies(ratings))


if __name__ == "__main__":
    print(Solution._candies([1,2,3,4,1,2,2,10,10,9,8,7,6,5]))
