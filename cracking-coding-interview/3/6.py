class Stack:
    def __init__(self):
        self._buf = []

    def push(self, data):
        self._buf.append(data)

    def pop(self):
        return self._buf.pop()
    
    def peek(self):
        return self._buf[-1]

    def is_empty(self):
        return len(self._buf) == 0

def insert_sort(stack):
    if stack.is_empty():
        return
    # Can use only one additional stack and no other data structure
    auxiliary_stack = Stack()
    while True:
        auxiliary_stack.push(stack.pop())
        while not stack.is_empty() and stack.peek() <= auxiliary_stack.peek():
            auxiliary_stack.push(stack.pop())

        if stack.is_empty():
            # Job finished
            while not auxiliary_stack.is_empty():
                stack.push(auxiliary_stack.pop())
            break

        # Find a proper place for the current top of `stack`
        temp = stack.pop()
        while not auxiliary_stack.is_empty() and temp > auxiliary_stack.peek():
            stack.push(auxiliary_stack.pop())
        stack.push(temp)
        while not auxiliary_stack.is_empty():
            stack.push(auxiliary_stack.pop())

def test_insert_sort():
    stack = Stack()
    v = [1, 2, 3, 100, 99, 98, 98, 4, 5, 0]
    for x in v:
        stack.push(x)

    insert_sort(stack)
    
    for x in sorted(v, reverse=True):
        assert stack.pop() == x
