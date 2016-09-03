class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        while i >= 0:
            if s[i] != ' ':
                break
            i -= 1
        j = i
        while j >= 0:
            if s[j] == ' ':
                break
            j -= 1

        return i - j


if __name__ == "__main__":
    assert Solution().lengthOfLastWord("") == 0
    assert Solution().lengthOfLastWord("   ") == 0
    assert Solution().lengthOfLastWord("   a   ") == 1
    assert Solution().lengthOfLastWord("a   ") == 1
    assert Solution().lengthOfLastWord("a") == 1
    assert Solution().lengthOfLastWord("abcd  haha") == 4
    assert Solution().lengthOfLastWord("abcd haha  ") == 4
