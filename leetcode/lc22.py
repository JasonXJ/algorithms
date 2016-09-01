class Solution(object):
    def generateParenthesis(self, n):
        used_left = 0
        balance = 0
        rv = []
        length = 2 * n
        buf = [None] * length

        i = 0
        while True:
            if i == length:
                rv.append(''.join(buf))

                # From right to left, find the first '(' that can be
                # converted to ')'
                while i > 0:
                    i -= 1
                    if buf[i] == '(':
                        if balance >= 2:
                            # This can be converted to ')'
                            buf[i] = ')'
                            balance -= 2
                            used_left -= 1
                            break
                        balance -= 1
                        used_left -= 1
                    else:  # buf[i] == ')'
                        balance += 1
                else:  # Cannot find a convertion point, break the outside loop
                    break
            elif used_left < n:  # Used left parenthesis first
                buf[i] = '('
                used_left += 1
                balance += 1
            else:  # Have to use right parenthesis
                buf[i] = ')'
                balance -= 1

            i += 1
        
        return rv

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
