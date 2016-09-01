# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).

class ListProxy:
    def __init__(self, lst, start=0, end=None):
        if end is None:
            end = len(lst)

        # Negative indices are also not supported here
        if not (0 <= start <= end <= len(lst)):
            raise ValueError

        self.lst = lst
        self.start = start
        self.length = end - start

    def __len__(self):
        return self.length

    def _check_range_or_die(self, v, allow_none=True):
        if v is None:
            if allow_none:
                return True
        else:
            # Not supporting negative index
            if 0 <= v < self.length:
                return True
        raise ValueError

    def _adjust_key_or_die(self, key_, is_slice_key=False):
        key = key_
        if not isinstance(key, int):
            raise TypeError
        if key < 0:
            key += self.length
        if 0 <= key < self.length:
            return key
        if is_slice_key:
            # A slice key is allowed to be >= self.length
            if key >= self.length:
                return self.length
        raise ValueError("Key out of range.")

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.lst[self.start + self._adjust_key_or_die(key)]
        elif isinstance(key, slice):
            if key.step is not None:
                raise ValueError
            new_start = self.start
            if key.start is not None:
                new_start += self._adjust_key_or_die(key.start, True)
            new_end = self.start
            if key.stop is None:
                new_end += self.length
            else:
                new_end += self._adjust_key_or_die(key.stop, True)
            return ListProxy(self.lst, new_start, new_end)
        else:
            raise TypeError

    def __iter__(self):
        raise NotImplementedError

    def __str__(self):
        return "ListProxy({})".format(self.lst)

    def __repr__(self):
        return self.__str__()
            

def odd_length(lst):
    return len(lst) & 1

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        return self._findMedianSortedArrays(ListProxy(nums1), ListProxy(nums2))

    def _findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 0:
            return self._median(nums2)
        if len(nums2) == 0:
            return self._median(nums1)

        if len(nums1) == 1:
            return self._medianOfArrayAndNumber(nums2, nums1[0])
        if len(nums2) == 1:
            return self._medianOfArrayAndNumber(nums1, nums2[0])

        # Both lists have at least two elements.

        median1 = self._median(nums1)
        median2 = self._median(nums2)

        # Array `a` has the larger (or equal) median
        if median1 >= median2:
            a_median = median1
            a = nums1
            b_median = median2
            b = nums2
        else:
            a_median = median2
            a = nums2
            b_median = median1
            b = nums1

        a_is_odd = odd_length(a)
        b_is_odd = odd_length(b)

        # This part find the numbers near medians. Note that because both
        # arrays have at least two elements, there will not be any "index out
        # of range"
        a_median_left = a[len(a)//2 - 1] # Parity does not matter
        if b_is_odd:
            b_median_right = b[len(b)//2 + 1]
        else:
            b_median_right = b[len(b)//2]

        # If we merge the two array and sort them, it will be look like
        # "----s----l----", where s/l is the smaller/larger median. We can
        # devide the merged array into 3 section, namely S1, S2, S3. The array
        # will look like this if we add the section label: "S1 s S2 l S3".
        # Note that the 3 sections never include s or l.
        # 
        # We say `s`/`l` exists if it corresponds to an element in the array
        # (and it is not an average of two elements)
        #
        # We have two cases: (Remember that array a has a larger median than
        # that of array b)
        #
        # Case 1: len(a) is odd OR len(b) is odd. In this case, we can prove
        # that the lengths of section S1 and S2 are both smaller than ``(len(a)
        # + len(b) - 1) // 2``, and so that we can safely delete any portion of
        # S1 and any portion of S2 as long as the two portions have the same
        # length. (By "safely", I means the median will still be the same).
        # Note that the "tail" of `a`, i.e. the portion of `a` that is to the
        # right of the median (not including the median), is inside section S3.
        # And the "head" of `b` is inside section S1. Let say `cut_size` equal
        # to min(a.tail, b.head), then we can delete a[:-cut_size] and
        # b[cut_size:] and process the new arrays recursively. Note that we do
        # not actually do any deletion, which is unnecessary and make the time
        # complexity larger.
        #
        #    Idea of proving maximum size of S1 (S2): We first calucate the
        #    minimum size S2 + S3. And we know that size(S1) = size(a) -
        #    size(b) - size(S2 + S3) - odd(a) - odd(b), where func odd() return
        #    1 if the array has a length of odd size, which means the median
        #    does exist.
        # 
        # Case 2: len(a) is even and len(b) is even. In this case, we can prove
        # that the lengths of section S1 and S2 are both smaller than ``(len(a)
        # + len(b)) // 2``. Unlike case 1, in this case the tail of `a` and the
        # head of `b` can cover the medians. So, to avoid deleting the medians,
        # we make the cut_size equal to min(a.tail-1, b.head-1)

        if a_is_odd or b_is_odd:
            # Case 1
            cut_size = min(len(a) // 2, len(b) // 2)
            assert cut_size > 0
        else:
            # Case 2
            cut_size = min(len(a) // 2 - 1, len(b) // 2 - 1)
            if cut_size == 0:
                # Case 2a: one of the array is too small so we collect the
                # candidates and calculate the median directly. Note that
                # ``len(candidates) <= 6`` so this does not affect the time
                # complexity.
                assert len(a) == 2 or len(b) == 2
                candidates = []
                for array in (a, b):
                    if len(array) == 2:
                        start = 0
                        end = 2
                    else: # len(array) >= 4
                        mid_high = len(array) // 2
                        start = mid_high - 2
                        end = mid_high + 2
                    for i in range(start, end):
                        candidates.append(array[i])
                assert len(candidates) <= 6
                candidates.sort()
                return self._median(candidates)
            # Case 2b: Do nothing here.

        return self._findMedianSortedArrays(a[:-cut_size], b[cut_size:])

    @staticmethod
    def _medianOfArrayAndNumber(array, number):
        # `array` is assumed to be sorted

        if len(array) == 0:
            return number
        elif len(array) == 1:
            return (array[0] + number) / 2.

        if len(array) & 1: # Odd length
            mid = len(array) // 2
            if number >= array[mid]:
                # ``array[mid+1]`` must exist because len(array) > 1
                if number <= array[mid+1]:
                    another = number
                else:
                    another = array[mid+1]
            else:
                # `array[mid-1]` must exist because len(array) > 1
                if number >= array[mid-1]:
                    another = number
                else:
                    another = array[mid-1]
            return (another + array[mid]) / 2.
        else:
            mid_high = len(array) // 2
            mid_high_value = array[mid_high]
            mid_low_value = array[mid_high-1]
            if mid_low_value <= number <= mid_high_value:
                return number
            elif number < mid_low_value:
                return mid_low_value
            else:
                return mid_high_value


    @staticmethod
    def _median(nums):
        # `nums` is assumed to be sorted
        mid = len(nums) // 2
        if odd_length(nums):
            return nums[mid]
        else:
            return (nums[mid-1] + nums[mid]) / 2.


def test_ListProxy():

    def compare_lst(l1, l2):
        assert len(l1) == len(l2)
        for i in range(len(l1)):
            assert l1[i] == l2[i]

    def compare_lst_item(l1, l2, index):
        assert l1[index] == l2[index]

    def compare_slice(l1, l2, slice_object):
        compare_lst(l1.__getitem__(slice_object), l2.__getitem__(slice_object))

    origin_lst = [chr(ord('a') + i) for i in range(6)]
    lp = ListProxy(origin_lst[:])
    compare_lst(lp, origin_lst)

    for i in range(6):
        compare_lst_item(lp, origin_lst, i)

    for i in range(-1, -7, -1):
        compare_lst_item(lp, origin_lst, i)

    test_slice_args = [
        [None],
        [0],
        [1],
        [-3],
        [-1],
        [None, 0],
        [None, 1],
        [None, 3],
        [None, 6],
        [None, -1],
        [None, -3],
        [None, -6],
        [0, 6],
        [0, -1],
        [0, 0],
        [3, 4],
        [2, 4],
        [-1, -1],
        [-3, -1],
        [-6, -6],
        [-6, -1],
        [-1, -1],
        [6, 6],
        [7, 11],
    ]

    for sa in test_slice_args:
        slice_object = slice(*sa)
        compare_lst(lp.__getitem__(slice_object), origin_lst.__getitem__(slice_object))

def test_solution_median():
    median = Solution._median

    assert median([1]) == 1
    assert median([1, 2]) == 1.5
    assert median([1, 2, 3]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    assert median([1, 2, 7, 10, 10]) == 7
    assert median([1, 2, 7, 7, 10, 10]) == 7

def test_solution_medianOfArrayAndNumber():
    func = Solution._medianOfArrayAndNumber

    # Special cases
    assert func([], 113) == 113
    assert func([87], 113) == 100

    # Odd
    assert func([10, 20, 30], 20) == 20
    assert func([10, 20, 30], 15) == 17.5
    assert func([10, 20, 30], 10) == 15
    assert func([10, 20, 30], 5) == 15
    assert func([10, 20, 30], 24) == 22
    assert func([10, 20, 30], 30) == 25
    assert func([10, 20, 30], 35) == 25

    # Even
    assert func([10, 20, 30, 40], 25) == 25
    assert func([10, 20, 30, 40], 20) == 20
    assert func([10, 20, 30, 40], 30) == 30
    assert func([10, 20, 30, 40], 15) == 20
    assert func([10, 20, 30, 40], 5) == 20
    assert func([10, 20, 30, 40], 35) == 30
    assert func([10, 20, 30, 40], 40) == 30


def test_solution():
    solution = Solution()
    func = solution.findMedianSortedArrays

    assert func([], [4,5,6,7,8]) == 6
    assert func([4,5,6,7,8], []) == 6

    assert func([1,2,3], [4,5,6]) == 3.5
    assert func([0,1,2,3], [4,5,6,7]) == 3.5
    assert func([-1,0,1,2,3], [4,5,6,7,8]) == 3.5

    assert func([1,2,3], [4,5,6,7]) == 4
    assert func([1,2,3], [4,5,6,7,8]) == 4.5
    assert func([1,2,3], [4,5,6,7,8,9]) == 5
    assert func([0,1,2,3], [4,5,6]) == 3
    assert func([-1,0,1,2,3], [4,5,6]) == 2.5
    assert func([-2,-1,0,1,2,3], [4,5,6]) == 2

    # Random Mixed
    import random
    for _ in range(1000):
        l1 = []
        l2 = []
        lst_lst = [l1, l2]
        size = random.randint(1, 50)
        for x in range(size):
            random.choice(lst_lst).append(x)

        assert func(l1, l2) == func(l2, l1) == solution._median(list(range(size)))
        pass
