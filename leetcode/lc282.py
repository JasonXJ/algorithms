class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if num == '':
            return []


        def compute(v1, op, v2, v3):
            """ This return the value of expression "v1 op v2 * v3", where
            v1/v2/v3 is integer and op is either "+" or "-". """
            if op == '+':
                return v1 + v2 * v3
            else:
                return v1 - v2 * v3

        components = []
        rv = []
        # `op0` is either '+' or '-'
        def search(start_index=0, v1=0, op0='+', v2=1):
            assert start_index < len(num)
            if num[start_index] == '0' and start_index < (len(num) - 1):
                # In this case, we need to avoid generating results like
                # "1*05". That is, if there is only one character (i.e. the
                # '0') left, we use it as the last value of the whole
                # expression as usual. Otherwise, we must add an operator
                # immediately after the '0'.
                allow_no_op = False
                op_range = (start_index + 1,)
            else:
                allow_no_op = True
                op_range = range(start_index + 1, len(num))

            for i in op_range:
                components.append(num[start_index:i])
                val = int(components[-1])

                # Handle '+' and '-'.  Since op is '+' or '-', we can finish
                # the calculation of "v1 op0 v2 * val".
                finished_new_v1 = compute(v1, op0, v2, val)
                for op in ('+', '-'):
                    components.append(op)
                    search(i, finished_new_v1, op, 1)
                    del components[-1]

                # Handle '*'
                new_v2 = v2 * val
                components.append('*')
                search(i, v1, op0, new_v2)
                del components[-2:]  # Remove the '*' and the last value

            if allow_no_op:
                # The whole left string will be used as a value
                if compute(v1, op0, v2, int(num[start_index:])) == target:
                    components.append(num[start_index:])
                    rv.append(''.join(components))
                    del components[-1]


        search()
        return rv



def test():
    def check(num, target, rv):
        assert sorted(Solution().addOperators(num, target)) == sorted(rv)
    check('123', 6, ["1+2+3", "1*2*3"])
    check('0', 0, ['0'])
    check('0', 1, [])
    check('232', 8, ["2*3+2", "2+3*2"])
    check('105', 5, ["1*0+5","10-5"])
    check('00', 0, ["0+0", "0-0", "0*0"])
    check("3456237490", 9191, [])
