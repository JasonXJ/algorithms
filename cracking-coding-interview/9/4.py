def all_subsets(s):
    s_lst = list(s)

    subsets = []
    
    def partial_subsets(base_set=tuple(), last_element_index=None):
        # Algorithm: Recursively add elements in `s_lst` with index larger than
        # `last_element_index` to `base_set` to construct new subsets. This
        # should be sufficient to avoid duplications.
        if last_element_index is None:
            range_start = 0
        else:
            range_start = last_element_index+1

        temp_list = list(base_set)
        temp_list.append(None)
        for index in range(range_start, len(s_lst)):
            temp_list[-1] = s_lst[index]
            new_set = frozenset(temp_list)
            subsets.append(new_set)
            partial_subsets(new_set, index)

    # Add empty set beforehand
    subsets.append(frozenset())

    partial_subsets()

    return subsets

def test_1(set_size=6):
    s = list(range(set_size))
    subsets = all_subsets(s)
    assert len(set(subsets)) == len(subsets) == 2**set_size
    return subsets

if __name__ == "__main__":
    for subset in test_1():
        print(subset)
