class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        def build_trie():
            root = {}
            for word in wordDict:
                if word == '':
                    # Empty word has no use at all and can make our searching
                    # process stuck.
                    continue
                cursor = root
                for x in word:
                    cursor = cursor.setdefault(x, {})
                cursor[None] = None  # Mark the end of a word

            return root
        

        trie = build_trie()
        failed_indexes = set()
        def search(index):
            if index in failed_indexes:
                return False
            cursor = trie
            while index < len(s):
                cursor = cursor.get(s[index])
                if cursor is None:
                    break
                elif None in cursor:
                    # This could be a breaking point.
                    if index == len(s) - 1:
                        return True
                    elif search(index + 1):
                        return True
                index += 1

            failed_indexes.add(index)
            return False


        return search(0)


def test():
    assert Solution().wordBreak('leetcode', ['leet', 'code'])
    assert Solution().wordBreak('leetcode', ['', 'leet', 'code'])


if __name__ == "__main__":
    test()
