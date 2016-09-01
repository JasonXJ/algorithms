#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

struct MyNumber {
    int num;
    int frequency;
};

bool compare_MyNumber(const MyNumber &n1, const MyNumber &n2) {
    return n1.frequency > n2.frequency;
}

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // An O(nlogn) implementation
        unordered_map<int,size_t> frequency;
        
        for (int i = 0; i < nums.size(); ++i) {
            unordered_map<int,size_t>::iterator it = frequency.find(nums[i]);
            if (it != frequency.end())
                ++(it->second);
            else
                frequency[nums[i]] = 1;
        }
        
        vector<MyNumber> temp;
        temp.reserve(frequency.size());
        for (unordered_map<int,size_t>::const_iterator it =
                frequency.cbegin(); it != frequency.cend(); ++it) {
            MyNumber my_number;
            my_number.num = it->first;
            my_number.frequency = it->second;
            temp.push_back(my_number);
        }

        sort(temp.begin(), temp.end(), &compare_MyNumber);

        vector<int> rv;
        rv.reserve(k);
        for (int i = 0; i < k; ++i) {
            rv.push_back(temp[i].num);
        }

        return rv;
    }
};

class FastSolution {
public:
    static inline void swap(vector<MyNumber> &target, const int i, const int j) {
        MyNumber temp_my_number;
        temp_my_number = target[i];
        target[i] = target[j];
        target[j] = temp_my_number;
    }
    static size_t partition(vector<MyNumber> &target, const int start, const int end) {
        int i, j;
        i = j = start;
        int medium_frequency = target[end-1].frequency;
        MyNumber temp_my_number;
        while (j != end - 1) {
            if (target[j].frequency > medium_frequency) {
                swap(target, i, j);
                ++i;
            }
            ++j;
        }
        swap(target, i, j);

        return i;
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        // An O(n) implementation
        unordered_map<int,size_t> frequency;
        
        for (int i = 0; i < nums.size(); ++i) {
            unordered_map<int,size_t>::iterator it = frequency.find(nums[i]);
            if (it != frequency.end())
                ++(it->second);
            else
                frequency[nums[i]] = 1;
        }

        vector<int> rv;
        rv.reserve(k);
        if (k >= frequency.size())
        {
            for (auto it = frequency.cbegin(); it != frequency.cend(); ++it) {
                rv.push_back(it->first);
            }
            return rv;
        }
        
        vector<MyNumber> temp;
        temp.reserve(frequency.size());
        for (unordered_map<int,size_t>::const_iterator it =
                frequency.cbegin(); it != frequency.cend(); ++it) {
            MyNumber my_number;
            my_number.num = it->first;
            my_number.frequency = it->second;
            temp.push_back(my_number);
        }

        int start = 0, end = temp.size();
        int split_point;
        while (true) {
            split_point = partition(temp, start, end);
            if (split_point < k)
                start = split_point + 1;
            else if (split_point > k)
                end = split_point;
            else
                break;
        }

        for (int i = 0; i < k; ++i)
            rv.push_back(temp[i].num);

        return rv;
    }
};

int main(int argc, char *argv[])
{
    FastSolution solution;
    vector<int> nums;
    nums.push_back(1);
    //nums.push_back(1);
    //nums.push_back(1);
    //nums.push_back(2);
    //nums.push_back(2);
    //nums.push_back(3);
    vector<int> topk = solution.topKFrequent(nums, 1);
    for (int i = 0; i < topk.size(); ++i) {
        cout << topk[i] << endl;
    }
    return 0;
}
