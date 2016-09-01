SLOT_SIZE = 4

def judge(guess, solution):
    assert len(solution) == len(guess) == SLOT_SIZE

    # Avoid changing the parameters
    guess_lst = list(guess)
    solution_lst = list(solution)

    hits = pseudo_hits = 0

    # First count the hits
    for i in range(SLOT_SIZE):
        assert guess_lst[i] is not None and solution_lst[i] is not None
        if guess_lst[i] == solution_lst[i]:
            hits += 1
            guess_lst[i] = None
            solution_lst[i] = None

    # Count the pseudo_hits
    for x in guess_lst:
        if x is None:
            continue
        for i in range(SLOT_SIZE):
            if solution_lst[i] == x:
                pseudo_hits += 1
                solution_lst[i] = None
                break

    return hits, pseudo_hits


def test_judge():
    assert judge("RGBY", "GGRR") == (1, 1)
    assert judge("RRGG", "GGRR") == (0, 4)
    assert judge("RRGG", "YYYR") == (0, 1)
    assert judge("RRGG", "RYYR") == (1, 1)
