class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in s:
            if x in ('(', '{', '['):
                stack.append(x)
            else:
                if x == ')':
                    if len(stack) == 0 or stack.pop() != '(':
                        return False
                elif x == '}':
                    if len(stack) == 0 or stack.pop() != '{':
                        return False
                elif x == ']':
                    if len(stack) == 0 or stack.pop() != '[':
                        return False
                else:
                    return False

        return len(stack) == 0
