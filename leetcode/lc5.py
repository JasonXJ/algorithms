def longest_palindromic_substring(s):
        if s == '':
            return 0

        # Use list for inner function visit. Python2 does not support nonlocal.
        max_start = [0]
        max_length = [1]

        def trace(l, r, initial_length):
            length = initial_length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 2
                l -= 1
                r += 1
            if length > max_length[0]:
                max_length[0] = length
                max_start[0] = l + 1

        # Case 1: Turn point is a character
        for turn_point in range(len(s)):
            l = turn_point - 1
            r = turn_point + 1
            trace(l, r, 1)

        # Case 2: Turn point is between two adjacent characters
        for turn_point_right in range(len(s)):
            l = turn_point_right - 1
            r = turn_point_right
            trace(l, r, 0)

        return s[max_start[0]:max_start[0]+max_length[0]]
