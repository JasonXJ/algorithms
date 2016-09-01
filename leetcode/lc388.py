class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        # Each element represents a directory, and the stored value is the
        # length including the `/`
        stack = [0]
        
        cursor = 0
        max_length = 0
        while cursor < len(input):
            # Read the `\t`s
            level = 0
            while cursor < len(input):
                if input[cursor] == '\t':
                    level += 1
                    cursor += 1
                else:
                    break

            # Alter the stack
            del stack[level+1:]

            # Read the name.
            # The code work for the last name which has no trailing `\n`
            name_start = cursor
            is_dir = True
            while cursor < len(input):
                if input[cursor] == '\n':
                    break
                if input[cursor] == '.':
                    is_dir = False
                cursor += 1
            name = input[name_start:cursor]
            cursor += 1

            if is_dir:
                # `+1` for the `/`
                stack.append(len(name) + 1 + stack[-1])
            else:
                length = len(name) + stack[-1]
                if length > max_length:
                    max_length = length

        return max_length


if __name__ == "__main__":
    f = Solution().lengthLongestPath
    assert f("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
