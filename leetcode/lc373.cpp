#include <unordered_set>
#include <vector>
#include <queue>
#include <cassert>
#include <functional>
#include <iostream>

using namespace std;


struct MyPair {
    size_t pos1, pos2;
    int sum;

    bool operator>(const MyPair &other) const {
        return sum > other.sum;
    }

    bool operator==(const MyPair &other) const {
        return pos1 == other.pos1 && pos2 == other.pos2;
    }
};

struct MyHash {
    size_t operator()(const MyPair &my_pair) const {
        return std::hash<size_t>()(my_pair.pos1) ^
            ((std::hash<size_t>()(my_pair.pos2) >> 1));
    }
};

class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        if (k == 0) {
            return vector<pair<int, int>>();
        }
        if (nums1.size() * nums2.size() <= (size_t) k) {
            vector<pair<int, int>> rv;
            for (auto it1 = nums1.begin(); it1 != nums1.end(); ++it1)
                for (auto it2 = nums2.begin(); it2 != nums2.end(); ++it2)
                    rv.push_back({*it1, *it2});
            return rv;
        }
        //assert(k > 0);
        //assert(nums1.size() > 0 && nums2.size() > 0);
        //assert(nums1.size() * nums2.size() >= (size_t) k);

        // TODO: use const
        vector<pair<int, int>> rv;
        priority_queue<MyPair, vector<MyPair>, greater<MyPair>> queue;
        unordered_set<MyPair, MyHash> seen_pairs;
        queue.push({0, 0, nums1[0] + nums2[0]});
        seen_pairs.insert(queue.top());

        while (rv.size() < (size_t) k) {
            assert(queue.size() > 0);

            size_t pos1 = queue.top().pos1, pos2 = queue.top().pos2;
            queue.pop();
            rv.push_back({nums1[pos1], nums2[pos2]});

            for (size_t pos1_delta = 0; pos1_delta <= 1; ++pos1_delta) {
                size_t new_pos1 = pos1 + pos1_delta,
                       new_pos2 = pos2 + (1 - pos1_delta);
                if (new_pos1 < nums1.size() && new_pos2 < nums2.size()) {
                    MyPair new_pair = {new_pos1, new_pos2, nums1[new_pos1] + nums2[new_pos2]};
                    if (seen_pairs.count(new_pair) == 0) {
                        seen_pairs.insert(new_pair);
                        queue.push(new_pair);
                    }
                }
            }
        }

        return rv;
    }
};

int main(int argc, char *argv[])
{
    (void) argc;
    (void) argv;

    Solution s;

    vector<int> nums1 = {1, 7, 10},
                nums2 = {2, 4, 6};
    
    const auto &rv = s.kSmallestPairs(nums1, nums2, 9);
    for (size_t i = 0; i < rv.size(); ++i)
        cout << rv[i].first << " " << rv[i].second << endl;

    return 0;
}
