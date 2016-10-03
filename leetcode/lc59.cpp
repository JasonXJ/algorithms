#include <vector>

using namespace std;


class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> rv;
        rv.resize(n);
        for (auto &v : rv) {
            v.resize(n);
        }
        
        int x = 0;
        int left_top = 0, right_bottom = n - 1;
        while(left_top < right_bottom) {
            // Top row;
            for (int i = left_top; i < right_bottom; ++i)
                rv[left_top][i] = ++x;
            // Right column.
            for (int i = left_top; i < right_bottom; ++i)
                rv[i][right_bottom] = ++x;
            // Bottom row;
            for (int i = right_bottom; i > left_top; --i)
                rv[right_bottom][i] = ++x;
            // Left column.
            for (int i = right_bottom; i > left_top; --i)
                rv[i][left_top] = ++x;
            ++left_top;
            --right_bottom;
        }

        if (left_top == right_bottom)
            rv[left_top][left_top] = ++x;

        return rv;
    }
};
