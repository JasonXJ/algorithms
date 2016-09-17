class TicTacToeNoBoard(object):
    class PlayerStatus(object):
        def __init__(self, n):
            self.rows = [0] * n
            self.cols = [0] * n
            self.dia = 0
            self.adia = 0


    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.players = [None, self.PlayerStatus(n), self.PlayerStatus(n)]


    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        ps = self.players[player]
        n = len(ps.rows)
        ps.rows[row] += 1
        ps.cols[col] += 1
        if row == col:
            ps.dia += 1
        if row + col == n - 1:
            ps.adia += 1
        if ps.rows[row] == n or ps.cols[col] == n or ps.dia == n or ps.adia == n:
            return player
        return 0



class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [[0] * n for _ in range(n)]
        self.n = n
        

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[row][col] = player
        if (all(self.board[row][x] == player for x in range(self.n))
                or all(self.board[x][col] == player for x in range(self.n))):
            return player
        if row == col and all(self.board[x][x] == player for x in range(self.n)):
            return player
        if (row + col == self.n - 1 and
                all(self.board[x][self.n - 1 - x] == player for x in range(self.n))):
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
