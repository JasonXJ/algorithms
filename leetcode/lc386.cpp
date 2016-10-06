#include <vector>

using namespace std;

class Solution {
    void lexicalOrder(int n, int val, vector<int>& rv) {
        int start = val==0?1:0;
        val *= 10;
        for (int i = start; i <= 9; ++i) {
            int temp = val + i;
            if (temp > n)
                return;
            rv.push_back(temp);
            lexicalOrder(n, temp, rv);
        }
    }
public:
    vector<int> lexicalOrder(int n) {
        vector<int> rv;
        lexicalOrder(n, 0, rv);
        return rv;
    }
};
