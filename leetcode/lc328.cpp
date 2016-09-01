#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};


class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (head == nullptr || head->next == nullptr)
            return head;

        ListNode *last_odd = head, *last_even = head->next, *to_be_moved_odd_node;
        
        while (last_even != nullptr && last_even->next != nullptr) {
            to_be_moved_odd_node = last_even->next;
            last_even->next = last_even->next->next;
            to_be_moved_odd_node->next = last_odd->next;
            last_odd->next = to_be_moved_odd_node;

            last_even = last_even->next;
            last_odd = to_be_moved_odd_node;
        }

        return head;
    }
};
