#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> ransom_counter, maga_counter;
        for (const char &c: ransomNote)
            ++ransom_counter[c];
        for (const char &c: magazine)
            ++maga_counter[c];
        for (const auto &x:ransom_counter) {
            if (maga_counter[x.first] < x.second)
                return false;
        }
        return true;
    }
};
