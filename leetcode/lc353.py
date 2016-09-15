from collections import deque

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        # Each element is a tuple of pairs ((x, y), (delta_x, delta_y)).
        self.head = (0,0)
        self.tail = (0,0)
        self.turning_points = deque()
        # XXX Quick and dirty fix: here we swap x[0] with x[1] because
        # internally we use x/y coordination, but the food position is in
        # row/col coordination.
        self.food = [(x[1],x[0]) for x in food]
        self.width = width
        self.height = height
        self.food_index = 0
        self.score = 0
        self.head_direction = 'R'
        self.tail_deltas = (1, 0)


    def _move_debug(self, direction):
        rv = self.move(direction)
        self._print_info()
        print('rv={}'.format(rv))


    def _print_info(self):
        print('head: {}, HD: {}, tail: {}, TD: {}, TPS: {}, FI: {}, score: {}'.format(
            self.head, self.head_direction, self.tail, self.tail_deltas,
            self.turning_points, self.food_index, self.score
        ))


    @staticmethod
    def _update_point(point, deltas):
        return point[0] + deltas[0], point[1] + deltas[1]


    @staticmethod
    def _on_line(point, line0, line1):
        if line0[0] == line1[0]:
            if point[0] == line0[0]:
                return min(line0[1], line1[1]) <= point[1] <= max(line0[1], line1[1])
        else:
            assert line0[1] == line1[1]
            if point[1] == line0[1]:
                return min(line0[0], line1[0]) <= point[0] <= max(line0[0], line1[0])


    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if direction == 'U':
            deltas = (0, -1)
        elif direction == 'D':
            deltas = (0, 1)
        elif direction == 'L':
            deltas = (-1, 0)
        else: # 'R'
            deltas = (1, 0)
        ori_head = self.head
        self.head = self._update_point(self.head, deltas)

        # Update turning points and head direction.
        if direction != self.head_direction:
            self.head_direction = direction
            self.turning_points.append((ori_head, deltas))

        if self.food_index < len(self.food) and self.head == self.food[self.food_index]:
            # Update score
            self.score += 1
            self.food_index += 1
        else:
            # Update tail if no food is eaten.
            if len(self.turning_points) > 0 and self.tail == self.turning_points[0][0]:
                self.tail_deltas = self.turning_points.popleft()[1]
            self.tail = self._update_point(self.tail, self.tail_deltas)

        # Check boarders.
        if not (0 <= self.head[0] < self.width and
                0 <= self.head[1] < self.height):
            return -1

        # Check biting self.
        if len(self.turning_points) > 0:
            if self._on_line(self.head, self.tail, self.turning_points[0][0]):
                return -1
            for i in range(len(self.turning_points) - 1):
                if self._on_line(self.head, self.turning_points[i][0],
                                 self.turning_points[i+1][0]):
                    return -1

        return self.score
    


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

if __name__ == "__main__":
    # sg = SnakeGame(5, 5, [])
    # sg._print_info()
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('D')
    # sg._move_debug('D')
    # sg._move_debug('D')
    # sg._move_debug('R')
    # sg._move_debug('U')
    # sg._move_debug('L')
    # sg._move_debug('D')
    # sg._move_debug('R')
    # sg._move_debug('L')
    # sg._move_debug('L')
    # sg = SnakeGame(5, 5, [[2,0]])
    # sg._print_info()
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('D')
    # sg._move_debug('D')
    # sg._move_debug('D')
    # sg._move_debug('R')
    # sg._move_debug('U')
    # sg._move_debug('L')
    # sg._move_debug('D')
    # sg._move_debug('R')
    # sg._move_debug('L')
    # sg._move_debug('L')
    # sg = SnakeGame(10, 10, [[2,0], [3,0], [4,0], [5,0], [6,0]])
    # sg._print_info()
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('D')
    # sg._move_debug('D')
    # sg._move_debug('D')
    # sg._move_debug('L')
    # sg._move_debug('D')
    # sg._move_debug('D')
    # sg._move_debug('D')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    # sg._move_debug('R')
    sg = SnakeGame(3, 2, [[1,2], [0,1]])
    sg._print_info()
    sg._move_debug('R')
    sg._move_debug('D')
    sg._move_debug('R')
    sg._move_debug('U')
    sg._move_debug('L')
    sg._move_debug('U')
