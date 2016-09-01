class Solution(object):
    def longestValidParentheses(self, s):
        # This should be an O(n) algorithm

        # Elements of stack are either '(' or integers. The integers represent
        # the lengths of "local" longest valid parentheses. So if we use 'i'
        # and 'p' to represent an integer and an '(' respectively, the stack
        # will conform the regex r'i?(p+i)*p+?'.

        stack = []
        balance = 0
        max_length = [0]

        def update_max_length():
            temp = max_length[0]
            for x in stack:
                if isinstance(x, int):
                    if x > temp:
                        temp = x
            max_length[0] = temp

        for x in s:
            if x == '(':
                stack.append('(')
                balance += 1
            else:  # x == ')'
                if balance == 0:
                    # Balance breaks. Empty the stack. We have to restart.
                    update_max_length()
                    del stack[:]
                else:
                    balance -= 1
                    if stack[-1] == '(':
                        # Case 1
                        stack.pop()
                        length = 2
                    else: # `stack[-1]` is an integer
                        # Case 2
                        length = stack.pop() + 2
                        stack.pop()  # pop the '('

                    if stack and isinstance(stack[-1], int):  # Mergable
                        stack[-1] += length
                    else:
                        stack.append(length)
        update_max_length()

        return max_length[0]
