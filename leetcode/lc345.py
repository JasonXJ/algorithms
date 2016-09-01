class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_lst = list(s)
        l = 0
        r = len(s) - 1
        vowels = 'aeiouAEIOU'
        while True:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1
            if l < r:
                s_lst[l], s_lst[r] = s_lst[r], s_lst[l]
                l += 1
                r -= 1
            else:
                break

        return ''.join(s_lst)


if __name__ == "__main__":
    assert Solution().reverseVowels('leetcode') == 'leotcede'
