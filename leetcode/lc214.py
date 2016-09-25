# O(n) solution using KMP.
class Solution(object):
    def shortestPalindrome(self, s):
        if s == '':
            return ''

        def generate_transition_table():
            table = [-1] * len(s)
            k = -1
            for i in range(1, len(s)):
                x = s[i]
                # Upon here, k == table[i-1].
                while k > -1 and s[k+1] != x:
                    k = table[k]
                if s[k+1] == x:
                    k += 1
                table[i] = k
            return table


        table = generate_transition_table()
        match = -1
        # Note that unlike standard KMP, here we match the longest prefix of s against
        # the suffix of s[::-1].
        for x in s[::-1]:
            while match > -1 and x != s[match+1]:
                match = table[match]
            if x == s[match+1]:
                match += 1

        # Upon here, s[match] is the last character of the longest prefix of s
        # which is also a suffix of s[::-1]; therefore, s[:match+1] is the
        # longest "prefix" palindrome of s.
        return s[match+1:][::-1] + s


# Compressing the string makes this solution much faster than `NaiveSolution`
# in some cases and allow this solution to pass the tests on Leetcode. However,
# the worst case complexity is actually not improved at all. So this solution
# is kind of a cheat.
class CompressedSolution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''

        compressed = []
        l = 0
        while l < len(s):
            r = l + 1
            while r < len(s) and s[l] == s[r]:
                r += 1
            compressed.append((s[l], r - l))
            l = r

        # Find the longest prefix palindrome from `s`
        for ri in range(len(compressed) - 1, 0, -1):
            if compressed[ri][0] == compressed[0][0] and compressed[ri][1] >= compressed[0][1]:
                li2 = 1
                ri2 = ri - 1
                while li2 < ri2:
                    if compressed[li2] != compressed[ri2]:
                        break
                    li2 += 1
                    ri2 -=1
                else:
                    # Longest palindrome found
                    break
        else:
            ri = 0

        uncompressed_ri = compressed[0][1]
        for ri2 in range(ri):
            uncompressed_ri += compressed[ri2][1]

        return s[uncompressed_ri:][::-1] + s


class NaiveSolution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        # Find the longest prefix palindrome from `s`
        for palindrome_right in range(len(s) - 1, 0, -1):
            i = 0
            j = palindrome_right
            while i < j:
                if s[i] != s[j]:
                    break
                i += 1
                j -= 1
            else:
                # Longest palindrome found
                break
        else:
            palindrome_right = 0

        return s[palindrome_right+1:][::-1] + s


def test():
    assert Solution().shortestPalindrome('aacecaaa') == 'aaacecaaa'
    assert Solution().shortestPalindrome('aaacecaaa') == 'aaacecaaa'
    assert Solution().shortestPalindrome('abcd') == 'dcbabcd'
    assert Solution().shortestPalindrome('abcd') == 'dcbabcd'
    assert Solution().shortestPalindrome('') == ''
    assert Solution().shortestPalindrome('a') == 'a'
