from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # `self.left_heap` is a max heap, `self.right_heap` is a min heap. Each
        # element in the heap is a 2-tuple ``(compare_value, actual_value)``.
        # We keep the following two conditions: 1. ``len(self.right_heap) -
        # len(self.left_heap) in (0, 1)``; 2. ``min(self.right_heap) >=
        # max(self.left_heap)``.
        self.right_heap = []
        self.left_heap = []


    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.right_heap) == 0 or num >= self.right_heap[0][1]:
            heappush(self.right_heap, (num, num))
        else:
            heappush(self.left_heap, (-num, num))
        
        len_different = len(self.right_heap) - len(self.left_heap)
        if len_different < 0:
            _, num2 = heappop(self.left_heap)
            heappush(self.right_heap, (num2, num2))
        elif len_different > 1:
            _, num2 = heappop(self.right_heap)
            heappush(self.left_heap, (-num2, num2))

        assert (len(self.right_heap) - len(self.left_heap)) in (0, 1)
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """

        if len(self.right_heap) > len(self.left_heap):
            return self.right_heap[0][1]
        else:
            return (self.left_heap[0][1] + self.right_heap[0][1]) / 2.


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    assert mf.findMedian() == 1
    mf.addNum(9)
    assert mf.findMedian() == 5, mf.findMedian()
    mf.addNum(-10)
    assert mf.findMedian() == 1
    mf.addNum(-20)
    assert mf.findMedian() == -4.5
