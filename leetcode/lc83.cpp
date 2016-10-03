struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};


class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *c1 = head;
        while (c1 != nullptr) {
            ListNode *c2 = c1->next;
            while (c2 != nullptr && c2->val == c1->val)
                c2 = c2->next;
            c1->next = c2;
            c1 = c1->next;
        }
        return head;
    }
};
