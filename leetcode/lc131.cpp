#include <vector>
#include <string>
#include <cassert>
#include <unordered_map>
#include <iostream>

using namespace std;

struct MyHash {
    size_t operator()(const pair<size_t,size_t> &p) const {
        return hash<size_t>()(p.first) ^ (hash<size_t>()(p.second) >> 1);
    }
};

class Solution {

    struct MySolution {
        const string &s;
        vector<vector<string>> rv;
        vector<size_t> start_points;
        // For each j in ``palindrome_lists[i]``, s[i:j] is a palindrome;
        vector<vector<size_t>> palindrome_lists;

        MySolution(const string &s_): s(s_) {
            if (s.size() > 0) {
                palindrome_lists.resize(s.size());
                for (size_t start = 0; start < s.size(); ++start) {
                    vector<size_t> &list = palindrome_lists[start];
                    for (size_t end = start + 1; end <= s.size(); ++end)
                        if (is_palindrome(start, end))
                            list.push_back(end);
                }
                partition(0);
            }
        }

        void partition(size_t start_point) {
            if (start_point == s.size()) {
                // A final result has been generated;
                rv.push_back({});
                vector<string> &vec = rv.back();
                assert(start_points.size() > 0);
                size_t last_start_point = start_points.front();
                for (auto it = start_points.begin() + 1; it != start_points.end(); ++it) {
                    vec.push_back(s.substr(last_start_point, *it - last_start_point));
                    last_start_point = *it;
                }
                vec.push_back(s.substr(last_start_point, s.size() - last_start_point));
            } else {
                start_points.push_back(start_point);
                auto palindrome_list = palindrome_lists[start_point];
                for (auto next_start_it = palindrome_list.begin();
                        next_start_it != palindrome_list.end();
                        ++next_start_it) {
                    partition(*next_start_it);
                }
                start_points.pop_back();
            }
        }

        bool is_palindrome(size_t start, size_t end) {
            size_t left = start, right = end - 1;
            while (right > left) {
                if (s[left++] != s[right--]) {
                    return false;
                }
            }

            return true;
        }
    };

public:
    vector<vector<string>> partition(string s) {
        return MySolution(s).rv;
    }
};


int main(int argc, char *argv[])
{
    (void) argc;
    (void) argv;

    Solution s;
    auto result = s.partition("aab");
    for (auto row_it = result.begin(); row_it != result.end(); ++row_it) {
        for (auto substr_it = row_it->begin(); substr_it != row_it->end(); ++substr_it) {
            cout << *substr_it << " ";
        }
        cout << endl;
    }

    return 0;
}
