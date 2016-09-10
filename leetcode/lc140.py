class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def build_trie():
            root = {}
            for w in wordDict:
                if w == '':
                    # Empty string has no use at all and will make our search
                    # function stuck.
                    continue
                cursor = root
                for x in w:
                    cursor = cursor.setdefault(x, {})
                cursor[None] = None  # Mark the end of a word

            return root


        trie = build_trie()
        # A dict which maps indexes to a list of sentences.
        subsentences = {}
        def search(index):
            try:
                return subsentences[index]
            except KeyError:
                pass
            cursor = trie
            i = index
            rv = []
            while i < len(s):
                cursor = cursor.get(s[i])
                if cursor is None:
                    break
                elif None in cursor:
                    # Found an end of a word
                    if i + 1 == len(s):
                        rv.append(s[index:])
                        break
                    else:
                        sub_solutions = search(i+1)
                        if sub_solutions is not None:
                            string_head = s[index:i+1] + ' '
                            for ss in sub_solutions:
                                rv.append(string_head + ss)
                i += 1

            if len(rv) == 0:
                rv = None
            subsentences[index] = rv
            return rv

        rv = search(0)
        if rv is None:
            rv = []
        return rv


def test():
    def check(s, words, expected):
        assert sorted(Solution().wordBreak(s, words)) == sorted(expected)
    check("catsanddog", {"cat", "cats", "and", "sand", "dog"}, ['cats and dog', 'cat sand dog'])
