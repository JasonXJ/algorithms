class Solution(object):
    def findStrobogrammatic(self, n):
        assert n >= 0
        if n == 0:
            return []
        if n == 1:
            return ['0', '1', '8']
        letters = [None] * n
        rv = []

        def fill(left_index):
            if left_index == n // 2 and n & 1:
                # n is odd, there is one more value to fill.
                for x in ('0', '1', '8'):
                    letters[left_index] = x
                    fill(left_index + 1)
            elif left_index >= n // 2:
                rv.append(''.join(letters))
            else:
                if left_index == 0:
                    self_alike = ('1', '8')
                else:
                    self_alike = ('0', '1', '8')
                for x in self_alike:
                    letters[left_index] = letters[n - 1 - left_index] = x
                    fill(left_index + 1)
                for x, y in [('6', '9'), ('9', '6')]:
                    letters[left_index] = x
                    letters[n - 1 - left_index] = y
                    fill(left_index + 1)


        fill(0)
        return rv
        


class Solution2(object):
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
