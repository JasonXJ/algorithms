# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

from collections import deque

class Solution(object):
    def __init__(self):
        self.buf = deque()


    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        temp = [None] * 4
        while len(self.buf) < n:
            read4_count = read4(temp)
            self.buf.extend(temp[:read4_count])
            if read4_count < 4:
                break

        count = min(n, len(self.buf))
        for i in range(count):
            buf[i] = self.buf.popleft()

        return count
