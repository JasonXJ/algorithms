class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.max = maxNumbers
        # [0, range_higher) is the number has been asigned before
        self.range_higher = 0
        self.released = set()
        

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.released:
            return self.released.pop()
        if self.range_higher < self.max:
            self.range_higher += 1
            return self.range_higher - 1
        return -1
        

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        if self.range_higher <= number < self.max:
            return True
        return number in self.released
        

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if not self.check(number):
            self.released.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

def test():
    pd = PhoneDirectory(10)
    for i in range(10):
        assert pd.check(i)
    assert pd.check(10) == False
    assert pd.get() == 0
    assert pd.check(0) == False and pd.check(1)
    assert pd.get() == 1
    assert pd.check(0) == False and pd.check(1) == False and pd.check(2)
    pd.release(0)
    assert pd.check(0) and pd.check(1) == False and pd.check(2)
    assert pd.get() == 0
