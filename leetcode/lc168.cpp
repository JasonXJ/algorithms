#include <string>
#include <utility>

using namespace std;

class Solution {
public:
    string convertToTitle(int n) {
        string result;
        while (n != 0) {
            int m = n % 26;
            if (m != 0) {
                result.push_back('A' + m - 1);
                n /= 26;
            } else {
                // m == 0 and n != 0
                result.push_back('Z');
                n = (n - 26) / 26;
            }
        }
        
        // Reverse the result.
        for (int i = 0, j = result.size() - 1; i < j; ++i, --j) {
            swap(result[i], result[j]);
        }
        return result;
    }
};
