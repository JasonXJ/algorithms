class Solution(object):
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []

        rv = []
        word_length = len(words[0])
        assert word_length > 0
        word_dict = {}  # word -> available_count
        for w in words:
            if w in word_dict:
                word_dict[w] += 1
            else:
                word_dict[w] = 1

        def recover_count(divided, start, times):
            for i in range(start, start+times):
                word_dict[divided[i]] += 1

        # import pytest; pytest.set_trace()

        for offset in range(word_length):
            divided = self._divide(s, offset, word_length)
            cursor = 0
            while cursor < len(divided):
                start = cursor
                word_count = 0
                while cursor < len(divided):
                    current_word = divided[cursor]
                    cursor += 1

                    current_word_count = word_dict.get(current_word)
                    if current_word_count is None:  # Discard the whole sequence
                        break
                    elif current_word_count > 0:  # Success
                        word_dict[current_word] -= 1
                        word_count += 1
                    else: 
                        # assert current_word_count == 0
                        # Move forward `start` until we pass `current_word`.
                        # This is like borrow an available count from the first
                        # `current_word` after original `start`.
                        while True:
                            temp_word = divided[start]
                            if temp_word == current_word:
                                break
                            start += 1
                            word_count -= 1
                            word_dict[temp_word] += 1
                        # Move `start` to pass `current_word`. However, do not
                        # need to adjust `word_dict[current_word]`.
                        start += 1

                    # assert word_count <= len(words)
                    if word_count == len(words):  # Find a concatenation
                        rv.append(start*word_length+offset)
                        # Move forward start, to prepare for finding next one
                        recover_count(divided, start, 1)
                        start += 1
                        word_count -= 1
                recover_count(divided, start, word_count)

        return rv

    @staticmethod
    def _divide(string, offset, word_length):
        rv = []
        s = offset
        e = s + word_length
        while e <= len(string):
            rv.append(string[s:e])
            s = e
            e += word_length
        return rv


def test():
    f = Solution().findSubstring

    #         012345678901234567890123456
    assert f('abcabcdfabeabcababcd', list('abc')) == [0,1,2,3,11,12,13,16]
    assert f('abcabcdfabacabadbcaabdcbaad', list('aabc')) == [0,8,9,10,11,16,17,22]
    assert f('foobarfooxfoofoobarbar', ['foo', 'bar']) == [0,3,13]
    assert f('wordgoodgoodgoodbestword', ['word','good','best','good']) == [8]
    assert sorted(f('aaaaaaaa', ['aa', 'aa', 'aa'])) == [0, 1, 2]
