#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        assert(k >= 0);
        const size_t nrows = matrix.size(),
                     ncols = matrix[0].size();
        size_t kk = k;

        int low = matrix[0][0], high = matrix[nrows-1][ncols-1];
        int mid;

        while (low <= high) {
            mid = int((long(low) + long(high)) / 2);
            size_t count = 0;
            for (size_t i = 0; i < nrows; ++i) {
                auto row = matrix[i];
                count += upper_bound(row.begin(), row.end(), mid) - row.begin();
            }
            if (count >= kk)
                high = mid - 1;
            else if (count < kk)
                low = mid + 1;
        }

        return low;
    }
};
