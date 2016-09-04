class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for x in tokens:
            try:
                number = int(x)
            except:
                number = None
            if number is not None:
                stack.append(number)
            else:
                r = stack.pop()
                l = stack.pop()
                if x == '+':
                    stack.append(l+r)
                elif x == '-':
                    stack.append(l-r)
                elif x == '*':
                    stack.append(l*r)
                else:  # x == '/'
                    assert x == '/'
                    # Note that the int float stuff is needed to pass leetcode's tests
                    stack.append(int(float(l)/r))

        assert len(stack) == 1
        return stack[0]
