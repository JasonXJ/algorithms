class Point:
    def __init__(self, x=None, y=None, point=None):
        self.x = x
        self.y = y
        if point is not None:
            self.copy(point)


    def copy(self, point):
        self.x = point.x
        self.y = point.y


    def __getitem__(self, attrname):
        return getattr(self, attrname)
    

    def __setitem__(self, attrname, val):
        return setattr(self, attrname, val)


# A very complicated solution.
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        # vertical[0] is to the left side of vertical[1]
        vertical = [None, None]
        # horizon[0] is below horizon[1]
        horizon = [None, None]
        pos = Point(0, 0)
        last_pos = Point(None, None)


        def between(v, b1, b2):
            return min(b1, b2) <= v <= max(b1, b2)


        def range_overlap(r1, r2):
            if r1[0] > r1[1]:
                r1 = r1[::-1]
            if r2[0] > r2[1]:
                r2 = r2[::-1]
            return r1[0] <= r2[1] and r2[0] <= r1[1]


        for i, d in enumerate(x):
            mod_val = i % 4
            if mod_val == 0: # Up
                # The "vertical" boundary lines.
                v_ = vertical
                # The "horizon" boundary lines.
                h_ = horizon
                # v_[r_] is the "right vertical" boundary line.
                r_ = 1
                # h_[u_] is the "up horizonal" boundary line.
                u_ = 1
                x_ = 'x'
                y_ = 'y'
                adjusted_d = d
            elif mod_val == 1: # Left
                v_ = horizon
                h_ = vertical
                r_ = 1
                u_ = 0
                x_ = 'y'
                y_ = 'x'
                adjusted_d = -d
            elif mod_val == 2: # Down
                v_ = vertical
                h_ = horizon
                r_ = 0
                u_ = 0
                x_ = 'x'
                y_ = 'y'
                adjusted_d = -d
            else: # Right
                v_ = horizon
                h_ = vertical
                r_ = 0
                u_ = 1
                x_ = 'y'
                y_ = 'x'
                adjusted_d = d

            last_pos.copy(pos)
            pos[y_] += adjusted_d

            # Check crossing.
            if (v_[r_] is not None and
                    pos[x_] == v_[r_][0][x_] and
                    range_overlap((last_pos[y_], pos[y_]), (v_[r_][0][y_], v_[r_][1][y_]))):
                # Cross the right boundary.
                return True
            if (h_[u_] is not None and
                    between(pos[x_], h_[u_][0][x_], h_[u_][1][x_]) and
                    between(h_[u_][0][y_], pos[y_], last_pos[y_])):
                return True

            # Update lines array `v_`
            if (
                    # Update if the line has not been set.
                    v_[r_] is None or
                    # Case 1. See lc335.pdf.
                    between(pos[x_], v_[r_][0][x_], v_[1-r_][0][x_]) or
                    # Case 2.1 and 2.2. See lc335.pdf.
                    not between(pos[y_], v_[r_][0][y_], v_[r_][1][y_])
            ):
                v_[r_] = (Point(point=last_pos), Point(point=pos))
            else:
                # Case 2.3
                v_[1-r_] = v_[r_]
                v_[r_] = (Point(point=last_pos), Point(point=pos))


        return False


def test():
    assert Solution().isSelfCrossing([2,1,1,2]) == True
    assert Solution().isSelfCrossing([1,2,3,4]) == False
    assert Solution().isSelfCrossing([1,1,1,1]) == True
    assert Solution().isSelfCrossing([1,1,2,2,3,3,3]) == False
    assert Solution().isSelfCrossing([1,1,2,2,3,3,3,1]) == True
    assert Solution().isSelfCrossing([1,1,2,2,3,3,3,2]) == True
    assert Solution().isSelfCrossing([1,1,2,2,3,3,3,3]) == True
    assert Solution().isSelfCrossing([1,1,2,2,3,3,3,4]) == True
    assert Solution().isSelfCrossing([1,1,2,2,3,3,3,100]) == True
