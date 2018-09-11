class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        memory = {}

        # Return (in-glass, excessive)
        def search(row, glass):
            try:
                return memory[(row, glass)]
            except KeyError:
                pass
            if glass < 0 or glass > row:
                return (0, 0)
            if row == 0 and glass == 0:
                rv = (min(1, poured), max(poured-1, 0))
            else:
                in_ = search(row-1, glass-1)[1] / 2 + search(row-1, glass)[1] / 2
                rv = (min(1, in_), max(in_-1, 0))

            memory[(row, glass)] = rv
            return rv

        return search(query_row, query_glass)[0]
