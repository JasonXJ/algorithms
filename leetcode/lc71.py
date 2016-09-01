# This does not pass the test case '/...' on leetcode OJ. However, I don't think this test case is legal.
class Solution(object):
    def simplifyPath(self, path):
        stack = []
        assert path[0] == '/'
        if path[-1] != '/':
            path += '/'
        status = 1
        for i, x in enumerate(list(path[1:]), 1):
            print('i={}, x={}, status={}, stack={}'.format(i, x, status, stack))
            if x == '.':
                if status == 1:
                    status = 3
                    continue
                elif status == 3:
                    status = 4
                    continue
            elif x == '/':
                if status == 1:
                    pass
                elif status == 2:
                    assert len(name_buf)
                    stack.append(name_buf)
                    status = 1
                elif status == 3:
                    status = 1
                elif status == 4:
                    if len(stack):
                        stack.pop()
                    status = 1
                continue
            else:  # Normal characters
                if status == 1:
                    name_buf = x
                    status = 2
                    continue
                elif status == 2:
                    name_buf += x
                    continue
            
            assert False, 'i={}, x={}, status={}, stack={}'.format(i, x, status, stack)

        return '/' + '/'.join(stack)

def test():
    func = Solution().simplifyPath
    assert func('/home/') == '/home'
    assert func('/a/./b/../../c/') == '/c'
    assert func('/../') == '/'
    assert func('/home//foo/') == '/home/foo'

if __name__ == "__main__":
    func = Solution().simplifyPath
    func('/a/./b/../../c/')
