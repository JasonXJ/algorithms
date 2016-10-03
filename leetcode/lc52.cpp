#include <vector>
#include <algorithm>

using namespace std;


class Solution {
    vector<bool> dia;
    vector<bool> adia;
    vector<int> perm;
    
    int perm_and_count(size_t x) {
        if (x >= perm.size()) {
            return 1;
        }
        int rv = 0;
        for (size_t i = x; i < perm.size(); ++i) {
            swap(perm[i], perm[x]);
            int y = perm[x];
            int dia_index = x - y + perm.size() - 1;
            int adia_index = x + y;
            if (!dia[dia_index] && !adia[adia_index]) {
                dia[dia_index] = true;
                adia[adia_index] = true;
                rv += perm_and_count(x + 1);
                dia[dia_index] = false;
                adia[adia_index] = false;
            }
            swap(perm[i], perm[x]);
        }
        return rv;
    }
public:
    int totalNQueens(int n) {
        perm.resize(n);
        dia.resize(2*n - 1);
        adia.resize(2*n - 1);
        fill(dia.begin(), dia.end(), false);
        fill(adia.begin(), adia.end(), false);
        for (int i = 0; i < n; ++i)
            perm[i] = i;
        return perm_and_count(0);
    }
};


class SlowSolution {
    vector<bool> dia;
    vector<bool> adia;
    
    bool check_dia(const vector<int> &perm) {
        fill(dia.begin(), dia.end(), false);
        fill(adia.begin(), adia.end(), false);
        for (int y = 0; y < int(perm.size()); ++y) {
            int x = perm[y];
            if (dia[x - y + perm.size() - 1])
                return false;
            dia[x - y + perm.size() - 1] = true;
            if (adia[x + y])
                return false;
            adia[x + y] = true;
        }
        return true;
    }

    int perm_and_count(vector<int> &perm, size_t index) {
        if (index >= perm.size()) {
            if (check_dia(perm))
                return 1;
            return 0;
        }
        int rv = 0;
        for (size_t i = index; i < perm.size(); ++i) {
            swap(perm[i], perm[index]);
            rv += perm_and_count(perm, index + 1);
            swap(perm[i], perm[index]);
        }
        return rv;
    }
public:
    int totalNQueens(int n) {
        vector<int> perm;
        perm.resize(n);
        dia.resize(2*n - 1);
        adia.resize(2*n - 1);
        for (int i = 0; i < n; ++i)
            perm[i] = i;
        return perm_and_count(perm, 0);
    }
};
