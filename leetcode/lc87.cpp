#include <string>
#include <unordered_map>

using namespace std;

class Solution {
    bool isScramble2(const string &s1, const string &s2) {
        if (s1 == s2)
            return true;
        unordered_map<char,int> char_counts;

        // Has not rotated
        for (size_t i = 0; i < s1.length() - 1; ++i) {
            if (s1[i] != s2[i]) {
                ++char_counts[s1[i]];
                --char_counts[s2[i]];
                if (char_counts[s1[i]] == 0) {
                    char_counts.erase(s1[i]);
                }
                if (char_counts[s2[i]] == 0) {
                    char_counts.erase(s2[i]);
                }
            }
            if (char_counts.size() == 0 &&
                    isScramble2(s1.substr(0, i + 1), s2.substr(0, i + 1)) &&
                    isScramble2(s1.substr(i + 1, s1.length() - i - 1), s2.substr(i + 1, s1.length() - i - 1))
               )
                return true;
        }

        char_counts.clear();
        // Rotated
        for (size_t pivot = 0; pivot < s1.length() - 1; ++pivot) {
            size_t s2_pivot = s1.length() - 1 - pivot;
            if (s1[pivot] != s2[s2_pivot]) {
                ++char_counts[s1[pivot]];
                --char_counts[s2[s2_pivot]];
                if (char_counts[s1[pivot]] == 0) {
                    char_counts.erase(s1[pivot]);
                }
                if (char_counts[s2[s2_pivot]] == 0) {
                    char_counts.erase(s2[s2_pivot]);
                }
            }
            if (char_counts.size() == 0 &&
                    isScramble2(s1.substr(0, pivot + 1), s2.substr(s2_pivot, pivot + 1)) &&
                    isScramble2(s1.substr(pivot + 1, s1.length() - pivot - 1), s2.substr(0, s1.length() - pivot - 1))
               )
                return true;
        }

        return false;
    }

public:
    bool isScramble(string s1, string s2) {
        if (s1.length() != s2.length())
            return false;
        if (s1 == s2)
            return true;
        unordered_map<char,int> char_counts;
        for (size_t i = 0; i < s1.length(); ++i) {
            ++char_counts[s1[i]];
            --char_counts[s2[i]];
        }
        for (auto it = char_counts.begin(); it != char_counts.end(); ++it) {
            if (it->second != 0)
                return false;
        }

        return isScramble2(s1, s2);
    }


};
