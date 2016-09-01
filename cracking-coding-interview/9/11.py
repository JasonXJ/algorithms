
class Expression:
    def __init__(self, expression):
        assert len(expression) % 2  # This test is insufficient
        self.expression = expression

    def __len__(self):
        return len(self.expression)

    def __getitem__(self, key):
        return self.expression[key]

    def get_operator(self, operator_index):
        return self.expression[operator_index*2 + 1]

    def split_expression(self, operator_index):
        """ This function split at `operator_index` and return a pair of
        subexpressions """
        expression_index = operator_index*2 + 1
        return (Expression(self.expression[:expression_index]),
                Expression(self.expression[expression_index+1:]))

    @property
    def num_operators(self):
        return len(self.expression) // 2

    @staticmethod
    def from_raw_expression(raw_expression):
        splited = list(raw_expression)
        assert len(splited) % 2
        for i in range(0, len(splited), 2):
            assert splited[i] in ('0', '1'), 'The {}-th element {!r} should be "0" or "1"'.format(i, splited[i])
            splited[i] = int(splited[i])
        for i in range(1, len(splited), 2):
            assert splited[i] in ('&', '|', '^')
        return Expression(tuple(splited))

    def __str__(self):
        return str(self.expression)
        

def count_operators(expression):
    return len(expression) // 2

def operator_index_to_expression_index(index):
    return 2*index + 1

def solve_parentheses(raw_expression, expected_result):
    expression = Expression.from_raw_expression(raw_expression)

    def string_surround_parentheses(s):
        if len(s) > 1:
            return '(' + s + ')'
        else:
            return s

    def split_and_solve(expression, operator_index, expected_result1,
                        expected_result2):
        e1, e2 = expression.split_expression(operator_index)
        r1 = solve_parentheses_(e1, expected_result1)
        if len(r1) == 0:
            return []  # No need to continue
        r2 = solve_parentheses_(e2, expected_result2)
        results = []
        for x in r1:
            for y in r2:
                results.append(string_surround_parentheses(x) +
                               expression.get_operator(operator_index) +
                               string_surround_parentheses(y))
        return results
    
    def solve_parentheses_(expression, expected_result):
        # Case 1: The expression has a single element of 0 or 1.
        if len(expression) == 1:
            if expression[0] == expected_result:
                return [str(expression[0])]
            else:
                return []

        # Case 2: The expression contain multiple elements
        results = []
        # Loop and use different operators in the current step.
        for i in range(expression.num_operators):
            operator = expression.get_operator(i)
            if operator == '&':
                if expected_result == 1:
                    results.extend(split_and_solve(expression, i, 1, 1))
                else:
                    results.extend(split_and_solve(expression, i, 0, 0)
                            + split_and_solve(expression, i, 0, 1)
                            + split_and_solve(expression, i, 1, 0))
            elif operator == '|':
                if expected_result == 1:
                    results.extend(split_and_solve(expression, i, 1, 0)
                            + split_and_solve(expression, i, 0, 1)
                            + split_and_solve(expression, i, 1, 1))
                else:
                    results.extend(split_and_solve(expression, i, 0, 0))
            else:  # operator '^'
                if expected_result == 1:
                    results.extend(split_and_solve(expression, i, 1, 0)
                            + split_and_solve(expression, i, 0, 1))
                else:
                    results.extend(split_and_solve(expression, i, 1, 1)
                            + split_and_solve(expression, i, 0, 0))
        return results

    return solve_parentheses_(expression, expected_result)

if __name__ == "__main__":
    samples = [('1&1|0^1', 1), ('1&1|0^1', 0)]
    for e, r in samples:
        print('-- solving `{} == {}` --'.format(e, r))
        for x in solve_parentheses(e, r):
            print(x)
