#include <iostream>
#include <cstring>
#include <algorithm>
#include <utility>

using namespace std;

class Solution {
public:
    double champagneTower(int poured_, int query_row, int query_glass) {
        memset(inited, 0, sizeof(inited));
        poured = poured_;

        return search(query_row, query_glass).first;
    }

    std::pair<double, double> search(int row, int glass) {
        if (glass < 0 || glass > row)
        {
            return {0, 0};
        }
        if (inited[row][glass])
        {
            return inglass_and_excessive[row][glass];
        }
        std::pair<double, double>& rv = inglass_and_excessive[row][glass];
        if (row == 0 && glass == 0)
        {
            rv = {std::min(1, poured), std::max(poured-1, 0)};
        }
        else
        {
            double in = (search(row-1, glass-1).second + search(row-1, glass).second)/2;
            rv = {std::min(1., in), std::max(in-1, 0.)};
        }
        //cout << "(" << row << ", " << glass << ")=(" << rv.first << ", " << rv.second << ")" << endl;
        inited[row][glass] = true;
        return rv;
    }

private:
    std::pair<double, double> inglass_and_excessive[100][100];
    bool inited[100][100];
    int poured;
};


int main(void)
{
    Solution().champagneTower(100, 85, 39);

    return 0;
}
