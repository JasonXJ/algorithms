class Solution(object):
    def solveNQueens(self, n):
        rv = []
        current = [['.']*n for _ in range(n)]
        column_availablity = [True] * n
        slash_availablity = [True] * (2*n-1)  # /
        backslash_availablity = [True] * (2*n-1) # \

        slash_index = lambda row,col:row+col
        backslash_index = lambda row,col:row-col+n-1

        # Backtracking algorithm
        def inner(row):
            if row == n:
                # Finish: convert `current` and stored it in `rv`
                rv.append([''.join(r) for r in current])
                return
            for col in range(n):
                if column_availablity[col]:
                    si = slash_index(row, col)
                    bsi = backslash_index(row, col)
                    if slash_availablity[si] and backslash_availablity[bsi]:
                        column_availablity[col] = False
                        slash_availablity[si] = False
                        backslash_availablity[bsi] = False

                        current[row][col] = 'Q'
                        inner(row+1)
                        current[row][col] = '.'

                        column_availablity[col] = True
                        slash_availablity[si] = True
                        backslash_availablity[bsi] = True

        inner(0)
        return rv

if __name__ == "__main__":
    for x in Solution().solveNQueens(4):
        print(x)
