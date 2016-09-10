from random import randint

# O(n) time/space
class Solution(object):
    """ Explanation and proof:

    Algorithm
    =========
    
    We first use the O(n) partition algorithm (of quick sort) to find the
    medium of the array and reorder it as follows (note that for i \in [0,
    k-2], a_i can be any value smaller than m and for j \in [0, k-1], b_j can
    be any value larger than m)::

                a_0 a_1 a_2 ... a_{k-1} b_0 b_1 ... b_{k-1}
        value:  <=m <=m <=m     ==m     >=m >=m     >=m

    Example: 6 5 4 4 --> 4 4 6 5 (m == 4)

    If the length of the array is odd, similarly, we have::

                a_0 a_1 a_2 ... a_{k-1} a_k b_0 b_1 ... b_{k-1}
        value:  <=m <=m <=m     <=m     ==m >=m >=m     >=m

    Example: 6 5 4 4 4 --> 4 4 4 6 5 (m == 4)

    After doing this, we know that a_i <= m <= b_i. We reorder the array to
    generate the required order::

        a_{k-1} b_{k-1} a_{k-2} b_{k-2} ... a_1 b_1 a_0 b_0

    Example: 6 5 4 4 --> 4 4 6 5 (m == 4) --> 4 5 4 6

    if the length is odd, we reorder it similarly::

        a_{k} b_{k-1} a_{k-1} b_{k-2} ... a_2 b_1 a_1 b_0 a_0

    Example: 6 5 4 4 4 --> 4 4 4 6 5 (m == 4) -> 4 5 4 6 4


    Proof
    =====

    We will assume the length is odd in this proof. The proof for the case when
    the length is even is very similar.

    TODO: proof that the when the algorithm does not work, either (1) a_i = b_i
    or (2) a_i = b_{i-1}. (1) implies that there are k+2 values equal to m,
    thus we need at least k+1 values which do not equal to m. However, there
    are only 2k+1 values. (2) implies that there are k+1 values equal to m,
    thus we need at least k values which do not equal to m. In this case, if
    b_0 == m, we can prove that there is no solution; if b_0 > m, our algorithm
    generates the correct solution.



    """
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        partitioned_nums = nums[:]
        self.medium_partition(partitioned_nums)
        a_index = (len(nums) - 1) // 2
        b_index = len(nums) - 1
        b_index_stop = a_index
        nums_index = 0
        while b_index > b_index_stop:
            nums[nums_index] = partitioned_nums[a_index]
            nums[nums_index+1] = partitioned_nums[b_index]
            a_index -= 1
            b_index -= 1
            nums_index += 2
        if len(nums) & 1:
            nums[-1] = partitioned_nums[0]
        

    @staticmethod
    def medium_partition(nums):
        assert len(nums) >= 1
        l = 0
        h = len(nums) - 1
        medium = h // 2

        # Find the medium and partition `nums`
        while True:
            assert l <= h
            random_index = randint(l, h)
            nums[h], nums[random_index] = nums[random_index], nums[h]
            x = nums[h]
            i = j = l
            count = 0
            while j < h:
                swap = False
                if nums[j] < x:
                    swap = True
                elif nums[j] == x:
                    # Note that we use the parity of `count` to evenly
                    # distribute values equal to `x`
                    if count & 1:
                        swap = True
                    count += 1
                if swap:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            nums[i], nums[h] = nums[h], nums[i]
            if i == medium:
                break
            elif i < medium:
                l = i + 1
            else:
                h = i - 1

        # Move all the values equal to the medium to the middle
        medium_value = nums[medium]
        l = 0
        h = medium - 1
        while True:
            while l < h and nums[l] != medium_value:
                l += 1
            while l < h and nums[h] == medium_value:
                h -= 1
            if l >= h:
                break
            nums[l], nums[h] = nums[h], nums[l]
            l += 1
            h -= 1

        l = medium + 1
        h = len(nums) - 1
        while True:
            while l < h and nums[h] != medium_value:
                h -= 1
            while l < h and nums[l] == medium_value:
                l += 1
            if l >= h:
                break
            nums[l], nums[h] = nums[h], nums[l]
            l += 1
            h -= 1


def test():
    import random
    from collections import Counter
    def subtest(array):
        counter = Counter(array)
        for _ in range(10):
            random.shuffle(array)
            backup_array = array[:]
            Solution().wiggleSort(array)
            counter2 = Counter(array)
            assert counter == counter2
            for i in range(1, len(array), 2):
                assert array[i-1] < array[i]
                assert i + 1 >= len(array) or array[i] > array[i+1]

    subtest([1,3,2,2,3,1])
    subtest([1,2,3,4,5,6])
    subtest([1,2,3,4,5])
    subtest([4,3,3,3,5])
    subtest([4,3,3,3,5,6])
    subtest([1,3,3,3,2,2])
    subtest([4,5,5,6])
    subtest([5])
    subtest([5,4])
    subtest([4,4,5])
    subtest([3,4,5])
