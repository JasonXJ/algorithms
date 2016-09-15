class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_mapping = {w:i for i, w in enumerate(words)}
        rv = []
        for i, word in enumerate(words):
            for prefix_length in range(len(word)+1):
                prefix = word[:prefix_length]
                reversed_prefix = prefix[::-1]
                suffix = word[prefix_length:]
                reversed_suffix = suffix[::-1]
                if prefix == reversed_prefix:
                    # Prefix is a palindrome.
                    j = word_mapping.get(reversed_suffix, i)
                    if j != i:
                        rv.append([j, i])
                # The ``len(suffix) != 0`` is for deduplication.
                if len(suffix) != 0 and suffix == reversed_suffix:
                    # suffix is a palindrome
                    j = word_mapping.get(reversed_prefix, i)
                    if j != i:
                        rv.append([i, j])

        return rv


def test():
    def check(arg, output):
        assert sorted(Solution().palindromePairs(arg)) == sorted(output)


    check(["bat", "tab", "cat"], [[0,1],[1,0]])
    check(["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]])
    check(['a',''], [[0,1],[1,0]])
