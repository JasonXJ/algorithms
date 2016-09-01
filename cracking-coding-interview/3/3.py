class SetOfStacks:
    def __init__(self, single_stack_limit=2):
        class _NoDataSentinel:
            def __len__(self):
                return single_stack_limit

        if single_stack_limit <= 0:
            raise ValueError("Stack limit must be larger then 0")
        self._single_stack_limit = single_stack_limit
        self._stacks = [_NoDataSentinel()]

    def push(self, data):
        if len(self._stacks[-1]) == self._single_stack_limit:
            self._stacks.append([data])
            print('A new substack created')
        else:
            self._stacks[-1].append(data)

    def pop(self):
        if len(self._stacks[-1]) == 0:
            print('Destroy a substack')
            del self._stacks[-1]
        return self._stacks[-1].pop()
    
    def pop_at(self, pos):
        # like ``self.pop()``, we always destroy empty top substack at the
        # begininng (so that always at most one empty stack at the top)
        if len(self._stacks[-1]) == 0:
            print('Destroy a substack')
            del self._stacks[-1]

        stack_no, offset = divmod(pos, self._single_stack_limit)
        stack_no += 1 # Skip first item (the ``_NoDataSentinel()``)

        to_return = self._stacks[stack_no].pop(offset)

        if stack_no + 1 != len(self._stacks):
            # need to move items
            stack_dest_no = stack_no
            stack_source_no = stack_no + 1
            while stack_source_no < len(self._stacks):
                self._stacks[stack_dest_no].append(self._stacks[stack_source_no].pop(0))

                stack_dest_no += 1
                stack_source_no += 1
        
        return to_return

def test_SetOfStacks():
    import pytest
    sstacks = SetOfStacks()
    v = [1,2,3,4,5]
    for x in v:
        sstacks.push(x)
    for x in reversed(v):
        assert sstacks.pop() == x

    with pytest.raises(AttributeError):
        sstacks.pop()

def test_SetOfStacks_interleave():
    import pytest
    sstacks = SetOfStacks()
    sstacks.push(1)
    sstacks.push(2)
    assert sstacks.pop() == 2
    assert sstacks.pop() == 1
    sstacks.push(3)
    assert sstacks.pop() == 3

    with pytest.raises(AttributeError):
        sstacks.pop()

def test_SetOfStacks__pop_at():
    import pytest
    def test(sstacks):
        v = [1,2,3,4,5]
        for x in v:
            sstacks.push(x)
        for x in v[1:]:
            assert sstacks.pop_at(1) == x
        assert sstacks.pop() == 1

        with pytest.raises(AttributeError):
            sstacks.pop()

    test(SetOfStacks())
    test(SetOfStacks(1))

