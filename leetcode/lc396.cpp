#include <vector>

using namespace std;

class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        // Assume that no overflow happens.
        if (A.size() == 0)
            return 0;

        int sum = 0;
        for (auto &x: A) {
            sum += x;
        }

        int num = 0;
        for (size_t i = 0; i < A.size(); ++i) {
            num += i * A[i];
        }

        int largest = num;
        for (size_t i = 0; i < A.size() - 1; ++i) {
            num = (num - sum) + A.size() * A[i];
            if (num > largest) {
                largest = num;
            }
        }

        return largest;
    }
};
