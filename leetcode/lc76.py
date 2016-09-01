class Solution(object):
    def minWindow(self, s, t):
        if t == '':
            return ''

        count = {}
        for c in t:
            count[c] = count.get(c, 0) - 1
        missing = -sum(count.values())
        min_width = len(s) + 1
        best_start = best_end = 0
        start = 0
        end = 0
        while end < len(s):
            # First step, move `end` to find a valid window.
            while end < len(s) and missing != 0:
                current_char = s[end]
                end += 1
                current_char_count = count.get(current_char)
                if current_char_count is not None:
                    if current_char_count < 0:
                        missing -= 1
                    count[current_char] += 1

            if missing != 0:  # Cannot find all character
                break

            # Second step, move `start` to shrink the window.
            while True:
                current_char = s[start]
                current_char_count = count.get(current_char)
                
                if current_char_count == 0:
                    # Update the minimum window.
                    width = end - start
                    if width < min_width:
                        best_start = start
                        best_end = end
                        min_width = width
                    
                    # Prepare for next loop
                    start += 1
                    count[current_char] = -1
                    missing += 1
                    break
                elif current_char_count is not None:
                    count[current_char] -= 1
                start += 1
        return s[best_start:best_end]


def test():
    f = Solution().minWindow
    assert f('ADOBECODEBANC', 'ABC') == 'BANC'
    assert f('a', 'aa') == ''
    assert f('ADOBECODEBANC', 'ABCB') == 'BECODEBA'
