struct Point {
    int x;
    int y;
    Point() : x(0), y(0) {}
    Point(int a, int b) : x(a), y(b) {}
};


// ============================================


#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;


struct HashPair {
    size_t operator()(const pair<int,int>& p) const {
        return (hash<int>()(p.first) << 1) ^ hash<int>()(p.second);
    }
};

// O(n^2) solution.
class Solution {
public:
    int maxPoints(const vector<Point>& points) {
        int gmax = 0;
        for (auto it1 = points.begin(); it1 != points.end(); ++it1) {
            int same = 1;
            int x0 = 0;
            int y0 = 0;
            unordered_map<pair<int,int>, int, HashPair> counter;
            for (auto it2 = it1 + 1; it2 != points.end(); ++it2) {
                if (it1->x == it2->x && it1->y == it2->y)
                    same += 1;
                else if (it1->x == it2->x)
                    x0 += 1;
                else if (it1->y == it2->y)
                    y0 += 1;
                else {
                    int adjusted_x = it2->x - it1->x;
                    int adjusted_y = it2->y - it1->y;
                    if (adjusted_x < 0) {
                        adjusted_x = -adjusted_x;
                        adjusted_y = -adjusted_y;
                    }
                    /* Note that both of adjusted_x and adjusted_y do
                     * no equal 0 */
                    int d = gcd(adjusted_x, adjusted_y);
                    ++counter[{adjusted_x / d, adjusted_y / d}];
                }
            }
            int counter_max = 0;
            for (const auto &pair : counter) {
                if (pair.second > counter_max)
                    counter_max = pair.second;
            }
            gmax = max({gmax, x0 + same, y0 + same, same + counter_max});
        }

        return gmax;
    }

    int gcd(int a, int b) {
        a = abs(a);
        b = abs(b);
        while (true) {
            if (a < b)
                swap(a, b);
            int mod = a % b;
            if (mod == 0)
                return b;
            else
                a = mod;
        }
    }
};


// The following is a complex (and correct) O(n^2) solution.

struct Params {
    int a, b, c;

    bool operator==(const Params &other) const {
        return a == other.a && b == other.b && c == other.c;
    }
};

class HashParams {
public:
    size_t operator()(const Params &p) const {
        return ((hash<int>()(p.a) << 1) ^ hash<int>()(p.b)) ^ hash<int>()(p.c);
    }
};


class ComplexSolution {
public:
    int maxPointsX(const vector<Point>& points) {
        unordered_map<int,int> counter;
        for (const auto &point : points) {
            ++counter[point.x];
        }

        int max = 0;
        for (const auto &pair : counter)
            if (pair.second > max)
                max = pair.second;
        return max;
    }


    int maxPointsY(const vector<Point>& points) {
        unordered_map<int,int> counter;
        for (const auto &point : points) {
            ++counter[point.y];
        }

        int max = 0;
        for (const auto &pair : counter)
            if (pair.second > max)
                max = pair.second;
        return max;
    }

    int maxPointsNormal(const vector<Point>& points) {
        int max = 0;
        for (auto it1=points.cbegin(); it1 != points.cend(); ++it1) {
            unordered_map<Params, int, HashParams> counter;
            int same = 1;
            for (auto it2 = it1 + 1; it2 != points.cend(); ++it2) {
                if (it1->x == it2->x && it1->y == it2->y)
                    same += 1;
                else if (it1->x != it2->x && it1->y != it2->y) {
                    // The line is "ax + by + c = 0"
                    int a = it1->y - it2->y;
                    int b = -(it1->x - it2->x);
                    int c = -(a*it1->x + b*it1->y);
                    if (a < 0) {
                        a = -a;
                        b = -b;
                        c = -c;
                    }
                    int d;
                    if (c != 0) {
                        d = gcd(a, abs(b), abs(c));
                    } else {
                        d = gcd(a, abs(b));
                    }
                    a /= d;
                    b /= d;
                    c /= d;
                    ++counter[{a,b,c}];
                }
            }

            for (const auto &pair : counter)
                if (pair.second + same > max)
                    max = pair.second + same;
        }

        return max;
    }

    int gcd(int a, int b, int c) {
        return gcd(gcd(a, b), gcd(b, c));
    }

    int gcd(int a, int b) {
        while (true) {
            if (a < b)
                swap(a, b);
            int mod = a % b;
            if (mod == 0)
                return b;
            else
                a = mod;
        }
    }


    int maxPoints(const vector<Point>& points) {
        return max(max(maxPointsX(points), maxPointsY(points)), maxPointsNormal(points));
    }
};

#include <iostream>
#include <cassert>

int main(void)
{
    assert(2 == Solution().maxPoints({{0,0}, {1,1}, {1, -1}}));
    assert(3 == Solution().maxPoints({{0,0}, {1,1}, {0, 0}}));
    assert(3 == Solution().maxPoints({{0,0}, {-1,-1}, {2, 2}}));
    assert(4 == Solution().maxPoints({{0,0}, {1,1}, {2,2}, {3,3}, {-1,1}, {-2,2}}));
    assert(5 == Solution().maxPoints({{0,0}, {1,1}, {2,2}, {3,3}, {-1,1}, {-773,773}, {-1001,1001}, {-2001,2001}}));
    assert(5 == Solution().maxPoints({{0,0}, {1,1}, {2,2}, {3,3}, {-1,1}, {-773,773}, {-1001,1001}, {-2002,2002}}));
    return 0;
}
