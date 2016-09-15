class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0 or len(s) == 0:
            return 0
        li = 0
        character_count = {s[0]:1}
        longest_length = 1
        for ri in range(1, len(s)):
            c = s[ri]
            if c not in character_count:
                if len(character_count) == k:
                    # Need to make room for the new character
                    while True:
                        c2 = s[li]
                        li += 1
                        character_count[c2] -= 1
                        if character_count[c2] == 0:
                            del character_count[c2]
                            break
                character_count[c] = 1
            else:
                character_count[c] += 1
            
            longest_length = max(longest_length, ri - li + 1)

        return longest_length
    

    # This is for question No.159
    def lengthOfLongestSubstringTwoDistinct(self, s):
        return self.lengthOfLongestSubstringKDistinct(s, 2)


def test():
    assert Solution().lengthOfLongestSubstringKDistinct('eceba', 2) == 3
    assert Solution().lengthOfLongestSubstringKDistinct('eceba', 1) == 1
    assert Solution().lengthOfLongestSubstringKDistinct('eeceba', 1) == 2
    assert Solution().lengthOfLongestSubstringKDistinct('eeceee', 1) == 3
