class Solution(object):
    def combine(self, n, k):
        rv = []

        if k == 0 or k > n:
            return []
        
        current = []
        def recursive(i):
            if len(current) == k:
                rv.append(current[:])
                return

            left = k - len(current)
            if n - i + 1 == left:  # No choice but add all to `current`
                rv.append(current + list(range(i, n + 1)))
                return

            # Case 1: Don't use i
            recursive(i+1)
            
            # Case 2: use i
            current.append(i)
            recursive(i+1)
            current.pop()

        recursive(1)
        return rv

if __name__ == "__main__":
    for x in Solution().combine(4, 2):
        print(x)
