class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.row_index = 0
        self.col_index = 0
        self._skip_finished_rows()


    def _skip_finished_rows(self):
        while (self.row_index < len(self.vec2d) and
               self.col_index == len(self.vec2d[self.row_index])):
            self.row_index += 1
            self.col_index = 0
        

    def next(self):
        """
        :rtype: int
        """
        rv = self.vec2d[self.row_index][self.col_index]
        self.col_index += 1
        self._skip_finished_rows()
        return rv
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.row_index < len(self.vec2d)
