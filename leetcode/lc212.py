class TrieSolution(object):
    def findWords(self, board, words):
        if len(board) == 0 or len(board[0]) == 0 or len(words) == 0:
            return []
        nrows = len(board)
        ncols = len(board[0])

        def build_trie():
            trie = {}
            for word in words:
                cursor = trie
                for x in word:
                    cursor = cursor.setdefault(x, {})
                # This mark the end of a path
                cursor[None] = None

            return trie


        trie = build_trie()
        rv = []
        prefix = []
        def search(row, col, node):
            if None in node:  # Encounter the end of a word
                rv.append(''.join(prefix))
                del node[None]
            if 0 <= row < nrows and 0 <= col < ncols:
                char = board[row][col]
                next_node = node.get(char)
                if next_node is not None:
                    board[row][col] = '#'
                    prefix.append(char)
                    for row2, col2 in (
                            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
                    ):
                        search(row2, col2, next_node)
                        if len(next_node) == 0:
                            del node[char]
                            break
                    del prefix[-1]
                    board[row][col] = char


        for row in range(nrows):
            for col in range(ncols):
                search(row, col, trie)

        return rv



class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        words = set(words)
        if len(board) == 0 or len(board[0]) == 0:
            return []

        nrows = len(board)
        ncols = len(board[0])
        visited = [[False]*ncols for _ in range(nrows)]
        first_char_map = {}
        for row in range(nrows):
            for col in range(ncols):
                first_char_map.setdefault(board[row][col], []).append((row,col))


        def search(word, index, row, col):
            if index >= len(word):
                return True
            if not (0 <= row < nrows and 0 <= col < ncols):
                return False
            if visited[row][col]:
                return False
            if word[index] != board[row][col]:
                return False
            # Search next character
            visited[row][col] = True
            if (search(word, index + 1, row - 1, col) or
                    search(word, index + 1, row + 1, col) or
                    search(word, index + 1, row, col - 1) or
                    search(word, index + 1, row, col + 1)):
                visited[row][col] = False
                return True
            visited[row][col] = False
            return False


        rv = []
        for word in words:
            for row, col in first_char_map.get(word[0], []):
                if search(word, 0, row, col):
                    rv.append(word)
                    break

        return rv


def test():
    method = TrieSolution().findWords
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    assert method(board, ['oath', 'pea', 'eat', 'rain']) == ['oath', 'eat']
    assert method(board, ['oath', 'oath']) == ['oath']
