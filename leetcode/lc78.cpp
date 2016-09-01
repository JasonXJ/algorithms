#include <vector>

using namespace std;

class Solution {
    struct Solver {
        const vector<int> &nums;
        vector<int> current;
        vector<vector<int>> results;

        Solver(const vector<int> &nums_): nums(nums_) {
            solve(0);
        }

        void solve(size_t pos) {
            if (pos == nums.size())
                results.push_back(current);
            else {
                solve(pos + 1);
                
                current.push_back(nums[pos]);
                solve(pos + 1);
                current.pop_back();
            }
        }
    };

public:
    vector<vector<int>> subsets(vector<int>& nums) {
        return Solver(nums).results;
    }
};
