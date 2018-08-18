class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        singles = {}
        # Map from "next value" to a sub-map, which map "delta" to a list
        # [count_of_length_2, count_of_longer]
        subsequences = {}
        total_count = 0
 
        for x in A:
            for delta, count_list in subsequences.get(x, {}):
                total_count += count_list[0] + count_list[1]
                # FIXME: what if delta == 0? can we update subsequences here?
