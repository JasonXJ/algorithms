#include <vector>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
class NestedInteger {
  public:
    // Constructor initializes an empty nested list.
    NestedInteger();

    // Constructor initializes a single integer.
    NestedInteger(int value);

    // Return true if this NestedInteger holds a single integer, rather than a nested list.
    bool isInteger() const;

    // Return the single integer that this NestedInteger holds, if it holds a single integer
    // The result is undefined if this NestedInteger holds a nested list
    int getInteger() const;

    // Set this NestedInteger to hold a single integer.
    void setInteger(int value);

    // Set this NestedInteger to hold a nested list and adds a nested integer to it.
    void add(const NestedInteger &ni);

    // Return the nested list that this NestedInteger holds, if it holds a nested list
    // The result is undefined if this NestedInteger holds a single integer
    const vector<NestedInteger> &getList() const;
};

class Solution {
    struct Solver {
        size_t cursor;
        const string &s;
        vector<NestedInteger> stack;

        Solver(const string &s_): cursor(0), s(s_) {
            stack.push_back({});

            while (cursor < s.size()) {
                const char next_char = s[cursor];
                if (isdigit(next_char) || next_char == '-') {
                    stack.back().add(NestedInteger(read_next_int()));
                } else if (next_char == '[') {
                    stack.push_back({});
                    ++cursor;
                } else if (next_char == ']') {
                    stack[stack.size() - 2].add(stack.back());
                    stack.pop_back();
                    ++cursor;
                } else {
                    assert(next_char == ',');
                    ++cursor;
                }
            }
        }

        int read_next_int() {
            size_t start = cursor++;
            while (cursor < s.size() && isdigit(s[cursor])) {
                ++cursor;
            }
            return atoi(s.substr(start, cursor - start).c_str());
        }
    };

public:
    NestedInteger deserialize(string s) {
        Solver solver(s);
        assert(solver.stack.size() == 1);
        return solver.stack[0].getList()[0];
    }

};
