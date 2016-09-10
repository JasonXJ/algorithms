class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        rv = []
        prefix = []
        def backtrack(index):
            if index >= len(digits):
                rv.append(''.join(prefix))
                return
            for x in mapping[digits[index]]:
                prefix.append(x)
                backtrack(index+1)
                del prefix[-1]

        backtrack(0)
        return rv


def test():
    assert Solution().letterCombinations('23') == ["ad", "ae", "af", "bd", "be",
                                                 "bf", "cd", "ce", "cf"]
