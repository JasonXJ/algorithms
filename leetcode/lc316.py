# An O(n^2) solution
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        ord_a = ord('a')
        # NOTE We redefine `s` here.
        s = [ord(x) - ord_a for x in s]
        counter = [0]*26
        for x in s:
            counter[x] += 1
        rv = []
        for i, c in enumerate(s):
            if counter[c] is None:
                # This character has been processed
                continue
            assert counter[c] >= 1
            counter[c] -= 1
            if counter[c] == 0:
                # The current character is not removeable. We have no other
                # choices.
                rv.append(c)
                counter[c] = None
                continue

            # The current character is removeable. We find the first character
            # to the right of the current character such that it is NOT
            # removeable and it is lexicographically larger than or equal to
            # the current character. If there is a lexicographically smaller
            # character in-between, than we will not remove the current
            # character.
            j = i + 1
            smaller_found = False
            while j < len(s):
                c2 = s[j]
                if counter[c2] is None:
                    # c2 has been processed, ignore it.
                    j += 1
                    continue
                assert counter[c2] >= 1
                if c2 < c:
                    # Found the smaller 
                    smaller_found = True
                    break
                # c2 >= c
                if counter[c2] == 1:
                    # This character is not removeable and it is
                    # lexicographically larger/equal
                    break
                counter[c2] -= 1
                j += 1

            # Recover the counts of character in s[i+1:j]
            for k in range(i+1, j):
                c2 = s[k]
                if counter[c2] is not None:
                    counter[c2] += 1

            if not smaller_found:
                # Must use the current character
                rv.append(c)
                counter[c] = None

        return ''.join(chr(x + ord_a) for x in rv)


from collections import Counter

# O(n) solution using stack
class StackSolution(object):
    def removeDuplicateLetters(self, s):
        """ The idea is that we scan the string from the left to right and
        maintain a stack of characters. We try to keep the stack as
        lexicographically ascending as possible (because lexicographically
        ascending string is the "smallest" string).
        """
        stack = []
        counter = Counter(s)
        used = set()
        for x in s:
            counter[x] -= 1
            if x in used:
                # Ignore the current character if it is already in the stack.
                continue
            while len(stack) and stack[-1] > x and counter[stack[-1]] != 0:
                # The top of the stack is lexicographically larger than the
                # current character, and we know that we will encounter this
                # character again later (because ``counter[...]!=0``), so it is
                # safe to pop it so that the lexicographical order is
                # maintained as good as possible.
                used.remove(stack.pop())
            stack.append(x)
            used.add(x)

        return ''.join(stack)


def test():
    for S in (Solution, StackSolution):
        assert Solution().removeDuplicateLetters('bcabc') == 'abc'
        assert Solution().removeDuplicateLetters('cbacdcbc') == 'acdb'
        assert Solution().removeDuplicateLetters('ccacbaba') == 'acb'
