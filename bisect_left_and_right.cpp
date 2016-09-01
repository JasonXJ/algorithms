#include <cassert>
#include <vector>
#include <algorithm>
#include <iostream>

using std::vector;
using std::cin;
using std::cout;
using std::endl;

size_t lower_bound(const vector<int> &v, int val) {
    size_t l = 0, r = v.size() - 1;

    while (l <= r && r != size_t(-1)) {
        size_t mid = (l + r) / 2;
        if (v[mid] >= val) {
            r = mid - 1;
        }
        else
            l = mid + 1;
    }

    return (size_t) l;
}

size_t upper_bound(const vector<int> &v, int val) {
    size_t l = 0, r = v.size() - 1;

    while (l <= r && r != size_t(-1)) {
        size_t mid = (l + r) / 2;
        if (v[mid] > val)
            r = mid - 1;
        else
            l = mid + 1;
    }

    return (size_t) l;
}

int main(void)
{

    vector<int> v = {10, 10, 20, 20, 30, 30, 30};
    int x;

    cout << ">>> ";
    while (cin >> x) {
        cout << lower_bound(v, x) << ' ' << upper_bound(v, x) << endl;
        cout << std::lower_bound(v.begin(), v.end(), x) - v.begin() << ' '
            << std::upper_bound(v.begin(), v.end(), x) - v.begin() << endl;
        cout << ">>> ";
    }
    
    
    return 0;
}
