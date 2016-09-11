class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.index = 0
        def consume_spaces():
            while self.index < len(s) and s[self.index] == ' ':
                self.index += 1

        
        def read_int():
            consume_spaces()
            start = self.index
            self.index += 1
            while self.index < len(s) and s[self.index].isdigit():
                self.index += 1
            return int(s[start:self.index])


        def process_stack():
            if len(stack) <= 2 or stack[-1] == '(' or stack[-2] == '(':
                return
            r = stack.pop()
            op = stack.pop()
            l = stack.pop()
            assert len(stack) == 0 or stack[-1] == '('
            if op == '+':
                stack.append(l + r)
            else:
                assert op == '-'
                stack.append(l - r)


        consume_spaces()
        if self.index >= len(s):
            return 0
        stack = []
        expect_number_or_left_paren = True
        while self.index < len(s):
            if expect_number_or_left_paren:
                if s[self.index] == '(':
                    stack.append('(')
                    self.index += 1
                else:
                    expect_number_or_left_paren = False
                    stack.append(read_int())
                    process_stack()
            else:
                if s[self.index] == ')':
                    process_stack()
                    v = stack.pop()
                    if stack.pop() != '(' or not isinstance(v, int):
                        raise ValueError
                    stack.append(v)
                    process_stack()
                else:
                    assert s[self.index] in ('+', '-')
                    stack.append(s[self.index])
                    expect_number_or_left_paren = True
                self.index += 1
            consume_spaces()

        process_stack()
        assert len(stack) == 1
        return stack[-1]


def test():
    assert Solution().calculate('1 + 1') == 2
    assert Solution().calculate(' 2-1 + 2 ') == 3
    assert Solution().calculate('(1+(4+5+2)-3)+6+8') == 23
    assert Solution().calculate('(2+1+(4+5+2)-3)+6+8') == 25
    assert Solution().calculate('(2+(1)+(2)-(3)+(4+5+2)-3)+6+8') == 24
    assert Solution().calculate('1') == 1
    assert Solution().calculate('(((1)))') == 1
    assert Solution().calculate('((((1-(2-1)))))') == 0
