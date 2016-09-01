class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n >= 1
        l = 1
        r = n
        from_left = True
        bit_no = 0
        rv = 0

        while True:
            assert l <= r
            if l == r:
                rv |= l << bit_no
                break

            if from_left:
                survive_bit = 1 - l
                from_left = False
            else:  # from right
                survive_bit = 1 - (0x1 & r)
                from_left = True
            if l == 1 and survive_bit == 1:
                l = 0
            if (0x1 & r) == survive_bit:
                r >>= 1
            else:
                r = (r - 1) >> 1

            if survive_bit == 1:
                rv |= 1 << bit_no
            bit_no += 1
        
        return rv


if __name__ == "__main__":
    # rv = Solution().lastRemaining(4)
    # print(rv)
    for i in range(1,10):
        rv = Solution().lastRemaining(i)
        print('{}: {}'.format(i, rv))
