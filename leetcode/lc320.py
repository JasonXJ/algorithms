class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """

        rv = []
        prefix = []

        def generate(start_index=0, last_shortened=False):
            if start_index >= len(word):
                rv.append(''.join(prefix))
                return
            prefix.append(word[start_index])
            generate(start_index + 1, False)
            del prefix[-1]
            if not last_shortened:
                for i in range(1, len(word) - start_index + 1):
                    prefix.append(str(i))
                    generate(start_index + i, True)
                    del prefix[-1]

        generate()

        return rv


def test():
    assert Solution().generateAbbreviations('') == ['']
    assert sorted(Solution().generateAbbreviations('word')) == sorted(["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"])
