struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};


#include <vector>
#include <map>
#include <cassert>

using namespace std;


class SummaryRanges {
    map<int, Interval> start_to_interval;

    map<int, Interval>::iterator find(int val) {
        auto it = start_to_interval.upper_bound(val);
        if (it == start_to_interval.begin()) {
            // There is no interval starts before val
            return start_to_interval.end();
        }
        --it;  // `it` now point to the right most interval starting before `val`
        if (it->second.end < val)
            return start_to_interval.end();

        return it;
    }

    void merge(map<int, Interval>::iterator it1, map<int, Interval>::iterator it2) {
        assert(it1->second.end + 1 == it2->second.start);
        it1->second.end = it2->second.end;
        start_to_interval.erase(it2);
    }

public:
    /** Initialize your data structure here. */
    SummaryRanges() {
    }
    
    void addNum(int val) {
        if (find(val) != start_to_interval.end())
            return;
        auto insert_rv = start_to_interval.insert({val, Interval(val, val)});
        auto it = insert_rv.first;
        auto before = find(val - 1);
        if (before != start_to_interval.end()) {
            merge(before, it);
            it = before;
        }
        auto after = find(val + 1);
        if (after != start_to_interval.end()) {
            merge(it, after);
        }
    }

    vector<Interval> getIntervals() {
        vector<Interval> vit;
        vit.reserve(start_to_interval.size());
        for (auto it = start_to_interval.begin(); it != start_to_interval.end(); ++it)
            vit.push_back(it->second);

        return vit;
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * vector<Interval> param_2 = obj.getIntervals();
 */

#include <iostream>
#include <cstdio>

void print(SummaryRanges &sr) {
    auto intervals = sr.getIntervals();
    for (auto it = intervals.begin(); it != intervals.end(); ++it) {
        printf("(%d, %d), ", it->start, it->end);
    }
    printf("\n");
}

int main(void)
{
    SummaryRanges sr;
    sr.addNum(1);
    print(sr);
    sr.addNum(3);
    print(sr);
    sr.addNum(7);
    print(sr);
    sr.addNum(2);
    print(sr);
    sr.addNum(6);
    print(sr);

    return 0;
}
