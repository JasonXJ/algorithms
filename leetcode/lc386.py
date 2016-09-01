# An O(n) time and space solution (Note that the results is a list whose size
# is n, so this is the best prossible solution). However, it gets Time Limit
# Exceeded error on leetcode, which is totally crazy.

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0:
            return []

        rv = []

        def fill_rv(head_value=0):
            if head_value == 0:
                r = range(1, 10)
            else:
                r = range(10)
            promote_head_value = head_value * 10
            for i in r:
                new_value = promote_head_value + i
                if new_value > n:
                    return
                rv.append(new_value)
                fill_rv(new_value)

        fill_rv()
        return rv

if __name__ == "__main__":
    f = Solution().lexicalOrder
    print(f(13))
    print(f(23))
    f(4999999)
