class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        assert n >= 0

        self_the_same = ['0', '1', '8']
        pairs = [('6', '9'), ('9', '6')] + [(x,x) for x in self_the_same]

        if n == 0:
            return []
        if n == 1:
            return self_the_same[:]

        rv = []
        number = [None] * n
        ODD = n & 1
        MIDDLE = (n - 1) // 2
        RIGHT = n - 1

        # Note that this function assume that n >= 2
        def fill(left_index=0):
            if left_index > MIDDLE:
                rv.append(''.join(number))
            elif left_index == MIDDLE and ODD:
                for x in self_the_same:
                    if left_index == 0 and x == '0':
                        continue
                    number[left_index] = x
                    rv.append(''.join(number))
            else:
                for x, y in pairs:
                    if left_index == 0 and x == '0':
                        continue
                    number[left_index] = x
                    number[RIGHT - left_index] = y
                    fill(left_index + 1)

        fill()
        return rv


def test():
    def check(n, expected):
        assert sorted(Solution().findStrobogrammatic(n)) == sorted(expected)
    check(1, ['0', '1', '8'])
    check(2, ["11","69","88","96"])
    check(3, ['101','111','181','609','619','689','808','818','888','906','916','986'])
