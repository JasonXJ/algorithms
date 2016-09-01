class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        self.words = words
        self.words_cursor = 0
        self.maxWidth = maxWidth
        rv = []

        if len(self.words) == 0:
            return []

        while True:
            start, min_length = self.next_line()

            # Case 1: Last line.
            if self.words_cursor >= len(self.words):
                rv.append(' '.join(self.words[start:]) + ' '*(self.maxWidth - min_length))
                return rv

            # Case 2: One word
            if self.words_cursor - start == 1:
                rv.append(self.words[start] + ' '*(self.maxWidth - min_length))
            # Case 3: Others
            else:
                s = self.words[start]
                extra_spaces = self.maxWidth - min_length
                small_gap, remaining_space_count = divmod(
                    extra_spaces, self.words_cursor - start - 1)
                small_gap += 1
                for x in self.words[start+1:start+1+remaining_space_count]:
                    s += ' ' * (small_gap + 1) + x
                for x in self.words[start+1+remaining_space_count:self.words_cursor]:
                    s += ' ' * small_gap + x
                rv.append(s)


    def next_line(self):
        assert self.words_cursor < len(self.words)
        start = self.words_cursor
        min_length = len(self.words[start])
        self.words_cursor += 1
        while self.words_cursor < len(self.words):
            addition_length = len(self.words[self.words_cursor]) + 1
            if min_length + addition_length <= self.maxWidth:
                min_length += addition_length
                self.words_cursor += 1
            else:
                break
        return start, min_length


def test(word_lst, width, expected_result):
    rv = Solution().fullJustify(word_lst, width)
    for x in rv:
        print(repr(x))
    assert rv == expected_result
    print('OK')

if __name__ == "__main__":

    test(
        ["This", "is", "an", "example", "of", "text", "justification."],
        16,
        [
            "This    is    an",
            "example  of text",
            "justification.  ",
        ]
    )
    test(
        ["This", "is", "an", "example", "of", "text", "apple", 'pie.'],
        16,
        [
            "This    is    an",
            "example  of text",
            "apple pie.      ",
        ]
    )
    test(
        ["This", "is", "an", "example", "of", "verylongword", "apple", 'pie.'],
        16,
        [
            "This    is    an",
            "example       of",
            "verylongword    ",
            "apple pie.      ",
        ]
    )
    test(
        ["a", "b", "c", "d", 'e', "veryverylongword", "apple", 'pie.'],
        16,
        [
            "a   b   c   d  e",
            "veryverylongword",
            "apple pie.      ",
        ]
    )
    test(
        ["a", "b", "c", "d", 'e', "veryverylongword", "veryverylongword", "apple", 'pie.'],
        16,
        [
            "a   b   c   d  e",
            "veryverylongword",
            "veryverylongword",
            "apple pie.      ",
        ]
    )
