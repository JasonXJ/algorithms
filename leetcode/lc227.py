class Solution(object):
    class _Solver:
        def __init__(self, s):
            self.s = s
            self.cursor = 0
            self.stack = [self.next_unsigned_int()]

            while True:
                self.skip_spaces()
                if self.cursor >= len(self.s):
                    break
                operator = self.s[self.cursor]
                self.cursor += 1
                r = self.next_unsigned_int()
                if operator in ('*', '/'):
                    l = self.stack.pop()
                    if operator == '*':
                        self.stack.append(l*r)
                    else:
                        self.stack.append(l//r)
                elif operator in ('+', '-'):
                    self.finish_stack()
                    self.stack.append(operator)
                    self.stack.append(r)
                else:
                    raise ValueError

            self.finish_stack()

        def finish_stack(self):
            assert len(self.stack) in (1, 3)
            if len(self.stack) == 3:
                l, op, r = self.stack
                del self.stack[:]
                if op == '+':
                    self.stack.append(l + r)
                elif op == '-':
                    self.stack.append(l - r)
                else:
                    raise RuntimeError

        def skip_spaces(self):
            while self.cursor < len(self.s) and self.s[self.cursor] == ' ':
                self.cursor += 1

        def next_unsigned_int(self):
            self.skip_spaces()
            start = self.cursor
            while self.cursor < len(self.s) and self.s[self.cursor].isdigit():
                self.cursor += 1
            return int(self.s[start:self.cursor])


    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        return self._Solver(s).stack[0]

if __name__ == "__main__":
    f = Solution().calculate

    print(f('3+2*2'))
    print(f(' 3/2 '))
    print(f(' 3+5 / 2'))
    print(f(' 3+5 / 2 *2'))
