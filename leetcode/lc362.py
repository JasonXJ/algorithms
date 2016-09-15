from collections import deque

class HitCounter(object):
    EXPIRE_TIME = 5*60
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buf = deque()
        self.hit_count = 0


    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if len(self.buf) > 0 and self.buf[-1][0] == timestamp:
            self.buf[-1][1] += 1
        else:
            self.buf.append([timestamp, 1])
        self.hit_count += 1
        self.clean_buf(timestamp)


    def clean_buf(self, current_timestamp):
        threshold = current_timestamp - self.EXPIRE_TIME
        while len(self.buf) and self.buf[0][0] <= threshold:
            self.hit_count -= self.buf.popleft()[1]
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.clean_buf(timestamp)
        return self.hit_count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
