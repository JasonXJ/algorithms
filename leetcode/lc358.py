from collections import Counter
from itertools import chain

# An O(n) solution.
class Solution(object):
    """ O(n). It seems that there are other much simpler solutions using heap.
    And since the character set size is 26, their heap operations can be
    considered to have O(1) time, which leads to the overall O(n) complexity.
    The solution shown here has the merit of having O(n) time even if the
    character set size is unbounded.
    
    STEP 1: We first identify the most frequent letters and their frequency.
    Let's say there are two most frequent letters: 'a' and 'b'. Their frequency
    is F. Then we can create a string whose length is the same as the input
    string. We initialize it as follows::

        ab______ab______ab______ab...ab_____ab
          slot 1  slot 2  slot 3  ...  slot F-1

    Note that between each "ab", there is an empty slot waiting for filling.
    Obviously, the number of slots is F-1. The sizes of the slots are
    distributed as even as possible; that is to say, the larger slots is at
    most 1 character larger than the smaller slots. Also, the larger slots are
    to the left of the smaller slots.

    In this string, the shortest distance of 'a' or 'b' appear on the right
    most side, as demonstrated in the following figure. Let's denote this
    distance by D. if D < k, it is not possible that we can generate a valid
    answer; otherwise, we can continue to fill the string in a way that the
    shortest distance never falls below D. Therefore, the algorithm is correct.

        ab______ab______ab______ab...ab_____ab
                                     |      |
                                     └── D ─┘


    STEP 2: We fill the string with "wrappers" before with the others. A
    wrapper is a character whose frequency equals F-1. We will explain the
    reasons later.  Let's say there are two wrapper: 'c' and 'd'. We update the
    string as follows::

        abcd____abcd____abcd____ab...abcd___ab
          slot 1  slot 2  slot 3  ...  slot F-1

    STEP 3: After that, we fill the string with other characters. Let's say the
    first character is e and its frequency is 2. Note that the order of
    characters does not matter anymore, so the first character can be any one.
    We first fill slot 1 with 'e' and then slot 2. Since we run out of 'e', we
    continue with the next character (again, which one is the next one does not
    matter), say 'f' with a frequency of 3. We then fill slot 3, 4 and 5. If
    the last slot (i.e. slot F-1) is filled, we will start from slot 1 again.
    This process continue until all the characters are used.


    **Wrappers**
    
    "Wrappers" are those which can wrap from the end to the beginning and
    create problems. For example, the input is "aaabbcd" and k = 3. A valid
    answer is "abcabda". After step 1, the string is "a__a__a". Let's consider
    what might happen if step 2 is omit. In step 3, let say the order of
    characters happens to be 'c', 'b', 'd'. Then after processing 'c', the
    string is "ac_a__a". We continue with 'b', which lead to "ac_ab_a" and then
    "acbab_a". Note that the distance between the 'b's is 2 now because 'b'
    wrap from the end to the beginning.

    """

    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if str == '':
            return ''
        if k <= 1:
            return str
        letter_counts = Counter(str)
        max_frequency = max(letter_counts.values())
        most_frequent_letters = [
            letter
            for letter, frequency
            in letter_counts.items()
            if frequency == max_frequency
        ]
        for x in most_frequent_letters:
            del letter_counts[x]
        wrappers = [
            letter
            for letter, frequency
            in letter_counts.items()
            if frequency == max_frequency - 1
        ]
        for x in wrappers:
            del letter_counts[x]

        if max_frequency == 1:
            return str
        else:
            base_slot_size, remaining_spaces = divmod(
                len(str) - max_frequency * len(most_frequent_letters),
                max_frequency - 1
            )
        
        if base_slot_size + len(most_frequent_letters) < k:
            # Not possible
            return ''
        
        # Construct the framework (i.e. fill the most frequent letters and leave the empty slots)
        rv = [None] * len(str)
        slot_indexes = []
        rv_cursor = 0
        slot_sizes = [base_slot_size + 1] * remaining_spaces + \
            [base_slot_size] * (max_frequency - 1 - remaining_spaces)
        for slot_size in slot_sizes:
            for x in most_frequent_letters:
                rv[rv_cursor] = x
                rv_cursor += 1
            slot_indexes.append(rv_cursor)
            rv_cursor += slot_size
        for x in most_frequent_letters:
            rv[rv_cursor] = x
            rv_cursor += 1
        assert rv_cursor == len(rv)

        # Fill non-most-frequent letters one by one (wrappers first).
        slot_indexes_cursor = 0
        for x, count in chain([(x, max_frequency - 1) for x in wrappers], letter_counts.items()):
            for _ in range(count):
                rv[slot_indexes[slot_indexes_cursor]] = x
                slot_indexes[slot_indexes_cursor] += 1
                slot_indexes_cursor += 1
                if slot_indexes_cursor == len(slot_indexes):
                    slot_indexes_cursor = 0

        return ''.join(rv)


def test():
    def check(string, k, has_result):
        rv = Solution().rearrangeString(string, k)
        if not has_result:
            assert rv == ''
        else:
            assert Counter(rv) == Counter(string)
            last_appear = {}
            for i, x in enumerate(rv):
                assert i - last_appear.get(x, -k) >= k
                last_appear[x] = i

    check('aaabc', 3, False)
    check('aaabc', 2, True)
    check('abcdabcdabcab', 3, True)
    check('abcdabcdabcab', 4, False)
    check('abeabac', 3, True)
    check('aabbcc', 3, True)
