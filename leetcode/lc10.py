class Solution(object):
    def isMatch(self, s, p):
        assert len(p) == 0 or p[0] != '*'
        failed_cases = set()
        return self._isMatch(s, 0, p, self._forward_pi(p, -1), failed_cases)

    @staticmethod
    def _forward_pi(p, pi):
        if pi+2 < len(p) and p[pi+2] == '*':
            return pi + 2
        return pi + 1

    def _isMatch(self, s, si, p, pi, failed_cases):
        assert si <= len(s) and pi <= len(p)

        if (si, pi) in failed_cases:
            return False

        # Finish matching
        if pi == len(p) and si == len(s):
            return True

        def compare(string_char, pattern_char):
            return ((pattern_char == '.' and string_char is not None) or
                    pattern_char == string_char)
        
        s_current_char = None
        p_current_char = None
        
        if si < len(s):
            s_current_char = s[si]
        if pi < len(p):
            p_current_char = p[pi]

        if p_current_char == '*':
            # Option 1: Ignore the star
            temp_pi = self._forward_pi(p, pi)
            if self._isMatch(s, si, p, temp_pi, failed_cases):
                return True
            # Fall through to Option 2

            # Option 2: Match the star (and keep the star as the current char)
            # Note that `pi-1` is always safe. Also, `compare` is smart enough
            # to make sure pattern '.' cannot match `None`.
            rv = compare(s_current_char, p[pi-1]) and self._isMatch(s, si+1, p, pi, failed_cases)
        else:
            rv = compare(s_current_char, p_current_char) and self._isMatch(s, si+1, p, self._forward_pi(p, pi), failed_cases)

        if not rv:
            failed_cases.add((si, pi))
        return rv
