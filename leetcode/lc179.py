""" 
Note that in the following explanation we assume that all the numbers are
strings, so, for example, number '55' is LARGER than number '455'. The idea is
that given two numbers x and y, if len(x) <= len(y) and x is not a prefix of y,
then we just need to directly compare them and put the larger one in the front.
Examples: '98' > '979', so 98 should go first. '97' < '986', so '986' should go
first. However, if x is a prefix of y, then we need to compare x + y and y + x.
For example, for number '8' and '883', we will put '8' first because '8883' >
'8838'. The reason for that is that if x is a prefix of y, their comparison is kind of in a tie, so in the final string they will be put in a same region. Thus, inside this region, who go first depend on the order of their concatenation.

There is a more formal proof (I haven't actually read it carefully yet) published in 
https://discuss.leetcode.com/topic/36004/mathematical-proof-of-correctness-of-sorting-method
"""

from functools import cmp_to_key

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if all(x == 0 for x in nums):
            return '0'

        def numcmp(x, y):
            if x == y:
                return 0
            elif x + y < y + x:
                return -1
            return 1


        strnums = [str(x) for x in nums]
        strnums.sort(key=cmp_to_key(numcmp), reverse=True)
        return ''.join(strnums)



# Python2 only
class SimplifiedSolution:
    def largestNumber(self, nums):
        if all(x == 0 for x in nums):
            return '0'
        strnums = [str(x) for x in nums]
        strnums.sort(cmp=lambda x,y: cmp(x+y, y+x), reverse=True)
        return ''.join(strnums)


def test():
    for S in (Solution, SimplifiedSolution):
        assert S().largestNumber([3, 30, 34, 5, 9, 98]) == '998534330'
        assert S().largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247]) ==  '9609938824824769735703560743981399'
        assert S().largestNumber([1440,7548,4240,6616,733,4712,883,8,9576]) == '9576888375487336616471242401440'

