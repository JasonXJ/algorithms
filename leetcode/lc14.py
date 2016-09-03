class Solution(object):
	def longestCommonPrefix(self, strs):
		if len(strs) == 0:
			return ""
		elif len(strs) == 1:
			return strs[0]
		pattern = strs[0]
		i = 0
		while i < len(pattern):
			x = pattern[i]
			for string in strs:
				if i >= len(string) or string[i] != x:
					break
			else:
				i += 1
				continue
			break

		return pattern[:i]

if __name__ == "__main__":
    assert Solution().longestCommonPrefix([]) == ''
    assert Solution().longestCommonPrefix(["abc"]) == 'abc'
    assert Solution().longestCommonPrefix(["", ""]) == ''
    assert Solution().longestCommonPrefix(["abcd", "abd", "abc"]) == 'ab'
