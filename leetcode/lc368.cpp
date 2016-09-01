#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

class SlowSolution {
    struct Solver {
        vector<int> longest;
        vector<int> nums;
        vector<int> current_sequence;

        Solver(const vector<int> &nums_): nums(nums_) {
            sort(nums.begin(), nums.end());
            solve(0);
        }

        void solve(size_t pos_in_nums) {
            if (pos_in_nums == nums.size()) {
                if (current_sequence.size() > longest.size())
                    longest = current_sequence;
                return;
            }

            int current_num = nums[pos_in_nums];
            if (current_sequence.empty() || current_num % current_sequence.back() == 0) {
                current_sequence.push_back(current_num);
                solve(pos_in_nums + 1);
                current_sequence.pop_back();
            }
            if (current_sequence.size() + (nums.size() - (pos_in_nums + 1)) <= longest.size()) {
                /* No need to continue because this sequence cannot be
                 * longer than the longest one */
                return;
            }
            solve(pos_in_nums + 1);
        }
    };

public:
    vector<int> largestDivisibleSubset(const vector<int>& nums) {
        return Solver(nums).longest;
    }
};

class Solution {
    struct Solver {
        struct Node {
            size_t last_index;
            size_t length;
        };

        vector<int> sorted_nums;
        vector<Node> nodes;
        vector<int> result;

        Solver(const vector<int> &nums) {
            sorted_nums = nums;
            sort(sorted_nums.begin(), sorted_nums.end());
            nodes.resize(nums.size());

            for (size_t i = 0; i < sorted_nums.size(); ++i) {
                int current_num = sorted_nums[i];
                Node &current_node = nodes[i];
                size_t parent_length = 0;
                for (size_t j = 0; j < i; ++j) {
                    int considered_num = sorted_nums[j];
                    const Node &considered_node = nodes[j];
                    if (current_num % considered_num == 0 && considered_node.length > parent_length) {
                        parent_length = considered_node.length;
                        current_node.last_index = j;
                        current_node.length = parent_length + 1;
                    }
                }
                if (parent_length == 0) // No available parent node.
                {
                    current_node.last_index = size_t(-1);
                    current_node.length = 1;
                }
            }

            size_t max_length = 0;
            size_t max_length_node_index = max_length - 1;
            for (size_t i = 0; i < sorted_nums.size(); ++i) {
                if (nodes[i].length > max_length) {
                    max_length = nodes[i].length;
                    max_length_node_index = i;
                }
            }

            result.resize(max_length);
            size_t next_result_index = max_length - 1; 
            while (max_length_node_index != size_t(-1)) {
                result[next_result_index--] = sorted_nums[max_length_node_index];
                max_length_node_index = nodes[max_length_node_index].last_index;
            }
        }
    };

public:
    vector<int> largestDivisibleSubset(const vector<int>& nums) {
        return Solver(nums).result;
    }
};

#include <iostream>

int main(void)
{
    Solution s;
    auto rv = s.largestDivisibleSubset({1, 2, 4, 5, 8, 3, 9, 18, 36});
    for (auto it = rv.begin(); it != rv.end(); ++it) {
        cout << *it << endl;
    }
    return 0;
}
