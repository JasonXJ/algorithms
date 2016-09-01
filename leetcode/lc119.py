class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        rowIndex += 1  # XXX: Quick and dirty fix.
        bufs = [[1]*rowIndex, [1]*rowIndex]
        current_buf_index = 0

        for row_no in range(3, rowIndex + 1):
            current_buf = bufs[current_buf_index]
            last_buf = bufs[1-current_buf_index]

            for i in range(1, row_no - 1):
                current_buf[i] = last_buf[i-1] + last_buf[i]
            current_buf[row_no - 1] = 1

            current_buf_index = 1 - current_buf_index

        return bufs[1 - current_buf_index]

if __name__ == "__main__":
    print(Solution().getRow(3))
