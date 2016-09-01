#include <iostream>
#include <string>
#include <cstring>

using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size())
            return false;
        int dp_size = (s1.size() + 1) * (s2.size() + 1);
        char *dp = new char[dp_size];
        for (int i = dp_size - 1; i >= 0; --i)
            dp[i] = -1;
        bool rv = isInterleave2(s1, 0, s2, 0, s3, 0, dp);
        delete[] dp;
        return rv;
    }

    bool isInterleave2(string s1, int i1, string s2, int i2, string s3, int i3, char *dp) {
        int dp_index = i1 * (s2.size() + 1) + i2;
        if (dp[dp_index] != -1)
            return dp[dp_index];
        bool result;
        if (i3 == s3.size())
            result = true;
        else if (i1 < s1.size() && s1[i1] == s3[i3] && isInterleave2(s1, i1+1, s2, i2, s3, i3+1, dp))
            result = true;
        else if (i2 < s2.size() && s2[i2] == s3[i3] && isInterleave2(s1, i1, s2, i2+1, s3, i3+1, dp))
            result = true;
        else
            result = false;
        dp[dp_index] = result;
        return result;
    }
};

class SolutionNonRecursive {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size())
            return false;
        const int row_length = s2.size() + 1,
              col_length = s1.size() + 1;
        int dp_size = row_length * col_length;
        bool *dp = new bool[dp_size];
        dp[0] = true;

        // Init first row
        for (int col = 1; col < row_length; ++col)
            dp[col] = dp[col-1] && s2[col - 1] == s3[col - 1];

        // Init first col
        for (int dp_index = row_length, s1_index = 0; s1_index <
                s1.size(); dp_index += row_length, ++s1_index)
            dp[dp_index] = dp[dp_index - row_length] && s1[s1_index] == s3[s1_index];

        // Row by Row
        for (int row = 1; row < col_length; ++row) {
            int dp_index = row * row_length;
            for (int col = 1; col < row_length; ++col) {
                ++dp_index;
                dp[dp_index] = (dp[dp_index-1] && s3[row + col - 1] == s2[col - 1]) ||
                    (dp[dp_index-row_length] && s3[row + col - 1] == s1[row - 1]);
            }
        }

        return dp[dp_size-1];
    }
};

int main(int argc, char *argv[])
{
    SolutionNonRecursive solution;
    cout << solution.isInterleave("", "b", "b") << endl;
    cout << solution.isInterleave("a", "a", "aa") << endl;
    cout << solution.isInterleave("a", "c", "aa") << endl;
    cout << solution.isInterleave("aabcc", "dbbca", "aadbbcbcac") << endl;
    cout << solution.isInterleave("aabckc", "dbbca", "aadbbcbcakc") << endl;
    cout << solution.isInterleave("aabcc", "kbbca", "aadbbcbcac") << endl;
    cout << solution.isInterleave("aabcc", "dbbck", "aadbbcbcac") << endl;
    cout << solution.isInterleave("", "dbbck", "aadbbcbcac") << endl;
    cout << solution.isInterleave("", "", "") << endl;

    return 0;
}
