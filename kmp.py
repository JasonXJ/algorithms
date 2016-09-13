# An implementation of the KMP string matching algorithm.
# NOTE `test_random` might not pass in python2 environment.


def kmp_transition_table(pattern):
    # ``table[x]`` is "the position of the last character of the longest
    # proper suffix" of "the prefix of the pattern whose last character
    # located at x". More formally, ``pattern[:table[x]+1]`` is the longest
    # proper suffix of string ``pattern[:x+1]``. 
    table = [-1] * len(pattern)
    k = -1
    for i in range(1, len(pattern)):
        c = pattern[i]
        # Upon here, we have loop invariant ``k == table[i-1]``.
        while k > -1 and pattern[k+1] != c:
            k = table[k]
        if pattern[k+1] == c:
            k += 1
        table[i] = k

    return table


def kmp(text, pattern):
    if text == '' or pattern == '' or len(pattern) > len(text):
        return []
    if len(pattern) == len(text):
        return [0] if pattern == text else []


    transition_table = kmp_transition_table(pattern)
    match = -1
    rv = []
    for i, x in enumerate(text):
        # Upon here, ``pattern[:match+1]`` matches ``text[i-(match+1):i]``. We
        # can also say that ``pattern[match]`` is the last character of the
        # current matching pattern prefix.
        while match > -1 and pattern[match + 1] != x:
            match = transition_table[match]
        if pattern[match + 1] == x:
            match += 1
        if match == len(pattern) - 1:
            # An result found
            rv.append(i+1-len(pattern))
            match = transition_table[match]


    return rv


def test():
    assert kmp('', '') == []
    assert kmp('acacacacac', 'acac') == [0, 2, 4, 6]
    assert kmp('bacbababaabcbaba', 'aba') == [4, 6, 13]
    assert kmp('bacbababaabcbaba', 'ababaca') == []
    assert kmp('bacbababaabcbaba', 'bac') == [0]
    assert kmp('bacbababaabcbabac', 'bac') == [0, 14]
    assert kmp('bacbababaabcbabac', 'bak') == []
    assert kmp('bacbababaabcbabac', 'a') == [1,4,6,8,9,13,15]
    assert kmp('bacbababaabcbabac', 'k') == []
    assert kmp('bac', 'bacbababaabcbabac') == []
    assert kmp('bac', 'bac') == [0]
    assert kmp('bac', 'bdc') == []

    for pattern_length in range(1, 20):
        assert kmp('a'*20, 'a'*pattern_length) == list(range(20-pattern_length+1))
    for pattern_length in range(1, 20):
        assert kmp('ac'*20, 'ac'*pattern_length) == list(range(0, 40-2*(pattern_length-1), 2))
    for pattern_length in range(1, 20):
        assert kmp('abc'*20, 'abc'*pattern_length) == list(range(0, 60-3*(pattern_length-1), 3))


def test_random():
    import random
    import string
    from random import choice
    from io import StringIO

    random.seed(0)
    
    
    def generate_test_case(text_length, pattern_length, characters, insert_pattern_prob):
        pattern_io = StringIO()
        for _ in range(pattern_length):
            pattern_io.write(random.choice(characters))
        pattern = pattern_io.getvalue()

        text_current_length = 0
        text_io = StringIO()
        while text_current_length < text_length:
            if random.random() < insert_pattern_prob:
                text_io.write(pattern)
                text_current_length += len(pattern)
            else:
                text_io.write(random.choice(characters))
                text_current_length += 1
        text = text_io.getvalue()
        # Generate result using naive algorithm
        matches = []
        for i in range(len(text)-len(pattern)+1):
            if text[i:i+len(pattern)] == pattern:
                matches.append(i)

        return text, pattern, matches

    
    def check(text_length, pattern_length, characters=string.printable, insert_pattern_prob=0.1):
        text, pattern, matches = generate_test_case(text_length,
                                                    pattern_length, characters,
                                                    insert_pattern_prob)
        assert kmp(text, pattern) == matches
    for _ in range(500):
        check(20, 2, string.digits)
        check(1000, 10, string.printable)
        check(1000, 10, string.printable, 0.5)
        check(10000, 100, string.printable)


if __name__ == "__main__":
    print(kmp_transition_table('acac'))
    print(kmp('acacacac', 'acac'))
    print(kmp_transition_table('aaaa'))
    print(kmp('aaaaa', 'aaa'))
