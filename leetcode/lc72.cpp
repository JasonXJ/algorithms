#include <string>

using namespace std;


class Solution {
public:
    int minDistance(string word1, string word2) {
        const int nrows = word1.size() + 1;
        const int ncols = word2.size() + 1;
        int *distance = new int[nrows * ncols];
        distance[0] = 0;

        for (int i = 1; i < nrows; ++i)
            distance[i * ncols] = i;
        for (int i = 1; i < ncols; ++i)
            distance[i] = i;

        for (int r = 1; r < nrows; ++r)
            for (int c = 1; c < ncols; ++c) {
                int replace = distance[(r-1)*ncols + c - 1];
                if (word1[r-1] != word2[c-1])
                    ++replace;
                int insert = distance[r*ncols + c - 1] + 1;
                int del = distance[(r-1)*ncols + c] + 1;
                int min = replace<=insert?replace:insert;
                min = min<=del?min:del;
                distance[r*ncols + c] = min;
            }

        int rv = distance[nrows * ncols - 1];
        delete[] distance;

        return rv;
    }
};
