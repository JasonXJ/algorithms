class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        assert denominator != 0
        if numerator == 0:
            return '0'
        
        negative = False
        if numerator < 0:
            negative = not negative
            numerator = -numerator
        if denominator < 0:
            negative = not negative
            denominator = -denominator

        head_num, remain = divmod(numerator, denominator)
        if negative:
            head = '-'
        else:
            head = ''
        head += str(head_num)
        if remain == 0:
            return head
        head += '.'

        assert 0 < remain < denominator

        fraction_lst = []
        remain_to_pos = {}
        repeat_start = None
        while remain > 0:
            remain *= 10
            if remain in remain_to_pos:
                repeat_start = remain_to_pos[remain]
                break
            remain_to_pos[remain] = len(fraction_lst)
            x, remain = divmod(remain, denominator)
            fraction_lst.append(str(x))
        if repeat_start is not None:
            fraction_lst.insert(repeat_start, '(')
            fraction_lst.append(')')

        return head + ''.join(fraction_lst)

if __name__ == "__main__":
    f = Solution().fractionToDecimal
    assert f(1,2) == '0.5'
    assert f(2,1) == '2'
    assert f(2,3) == '0.(6)'
    assert f(1,6) == '0.1(6)'
    assert f(-1,2) == '-0.5'
    assert f(-2,1) == '-2'
    assert f(-2,3) == '-0.(6)'
    assert f(-1,6) == '-0.1(6)'
    assert f(1,-2) == '-0.5'
    assert f(2,-1) == '-2'
    assert f(2,-3) == '-0.(6)'
    assert f(1,-6) == '-0.1(6)'
    assert f(-1,-2) == '0.5'
    assert f(-2,-1) == '2'
    assert f(-2,-3) == '0.(6)'
    assert f(-1,-6) == '0.1(6)'
    assert f(0, 7) == '0'
