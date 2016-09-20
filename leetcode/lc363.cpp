#include <vector>
#include <climits>
#include <cassert>
#include <set>

using namespace std;

/* An O(m^2 * n * log n) solution, where m = min(nrows, ncols) and n =
 * max(nrows, ncols) */
class Solution {
    // MatrixProxy always has nrows <= ncols
    class MatrixProxy {
        const vector<vector<int>> &matrix;
        bool transpose;
        size_t nrows, ncols;
    public:
        MatrixProxy(const vector<vector<int>> &matrix_):matrix(matrix_) {
            size_t actual_rows = matrix.size();
            size_t actual_cols = matrix[0].size();
            if (actual_rows > actual_cols) {
                transpose = true;
                nrows = actual_cols;
                ncols = actual_rows;
            } else {
                transpose = false;
                nrows = actual_rows;
                ncols = actual_cols;
            }
        }

        int get(int row, int col) const {
            if (!transpose) {
                return matrix[row][col];
            } else {
                return matrix[col][row];
            }
        }

        size_t get_nrows() const {return nrows;}
        size_t get_ncols() const {return ncols;}
    };

public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        MatrixProxy mp = MatrixProxy(matrix);
        vector<vector<int>> cum_rows;
        cum_rows.reserve(mp.get_nrows() + 1);
        cum_rows.push_back({});
        // The first row of `cum_rows` is an all zero dummy row.
        cum_rows[0].resize(mp.get_ncols(), 0);
        for (size_t row = 0; row < mp.get_nrows(); ++row) {
            cum_rows.push_back({});
            vector<int> &pre_cum_row = cum_rows[cum_rows.size() - 2];
            vector<int> &cum_row = cum_rows.back();
            cum_row.reserve(mp.get_ncols());
            for (size_t col = 0; col < mp.get_ncols(); ++col) {
                cum_row.push_back(mp.get(row, col) + pre_cum_row[col]);
            }
        }

        vector<int> range_sum_row;
        range_sum_row.resize(mp.get_ncols());
        int rv = INT_MIN;
        for (size_t row1 = 0; row1 < cum_rows.size() - 1; ++row1) {
            for (size_t row2 = row1 + 1; row2 < cum_rows.size(); ++row2) {
                /* Note that at the begining of `cum_rows` there is an
                 * extra dummy row. So here we are searching all
                 * rectangles who start from row1 (inclusive) and end
                 * at row2 (exclusive) of `matrix`. */
                for (size_t col = 0; col < mp.get_ncols(); ++col)
                    range_sum_row[col] = cum_rows[row2][col] - cum_rows[row1][col];
                int temp = maxRangeSum(range_sum_row, k);
                assert(temp <= k);
                if (temp > rv)
                    rv = temp;
            }
        }

        return rv;
    }

    /* Return the maximum range sum of `row` that is no larger than k.
     * This function also guarantee that the range contains at least
     * one element. */
    static int maxRangeSum(const vector<int> &row, int k) {
        set<int> tree;
        tree.insert(0);
        int prefix_sum = 0;
        int rv = INT_MIN;
        for (size_t i = 0; i < row.size(); ++i) {
            prefix_sum += row[i];
            auto it = tree.lower_bound(prefix_sum - k);
            if (it != tree.end() && prefix_sum - *it >= rv)
                rv = prefix_sum - *it;
            tree.insert(prefix_sum);
        }

        return rv;
    }
};

#include <iostream>
int main(void)
{
    vector<vector<int>> matrix = {
        {1, 0, 1},
        {0, -2, 3}
    };
    cout << Solution().maxSumSubmatrix(matrix, 2) << endl;
    return 0;
}
