#include <vector>

using namespace std;

class NestedInteger {
  public:
    // Return true if this NestedInteger holds a single integer, rather than a nested list.
    bool isInteger() const;

    // Return the single integer that this NestedInteger holds, if it holds a single integer
    // The result is undefined if this NestedInteger holds a nested list
    int getInteger() const;

    // Return the nested list that this NestedInteger holds, if it holds a nested list
    // The result is undefined if this NestedInteger holds a single integer
    const vector<NestedInteger> &getList() const;
};


class NestedIterator {
    struct State {
        const vector<NestedInteger> *p_nested_list;
        size_t pos;

        State(const vector<NestedInteger> *p_nested_list) {
            this->p_nested_list = p_nested_list;
            pos = 0;
        }
    };
    vector<State> states;

public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        states.push_back(State(&nestedList));
    }

    /** 
     * After calling this function, either `states.empty()` or
     * `states.back().p_nested_list[last_state.pos].isInteger()`
     */
    void expand_and_clean() {
        while(!states.empty()) {
            State &last_state = states.back();
            if (last_state.pos >= last_state.p_nested_list->size()) {
                states.pop_back();
                continue;
            }
            const NestedInteger &current_element = last_state.p_nested_list->at(last_state.pos);
            if (current_element.isInteger())
                break;

            // `current_element` is a list and need to be expanded.
            ++last_state.pos;
            states.push_back(State(&current_element.getList()));
        }
    }

    int next() {
        expand_and_clean();
        State &last_state = states.back();
        return last_state.p_nested_list->at(last_state.pos++).getInteger();
    }

    bool hasNext() {
        expand_and_clean();
        return !states.empty();
    }
};
