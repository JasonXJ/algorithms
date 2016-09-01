def valid_parentheses(pairs):
    results = []
    
    def inner(prefix, remain_pairs, extra_close):
        assert remain_pairs >= 1

        new_prefix_base = prefix + '('  # Always add an '(' at the begining
        max_close = extra_close + 1
        new_remain_pairs = remain_pairs - 1
        
        if new_remain_pairs == 0:
            results.append(new_prefix_base + ')'*max_close)
        else:
            for i in range(max_close+1):
                inner(new_prefix_base+')'*i, new_remain_pairs, max_close-i)

    inner('', pairs, 0)
    return results

def check_valid(s):
    n = 0
    for c in s:
        if c == '(':
            n += 1
        elif c == ')':
            assert n > 0
            n -= 1
        else:
            assert False
    assert n == 0

def test_1(pairs=6):
    results = valid_parentheses(pairs)
    for s in results:
        check_valid(s)
    return results

if __name__ == "__main__":
    for s in test_1():
        print(s)
