struct ListNode {
 int val;
 ListNode *next;
 ListNode(int x) : val(x), next(nullptr) {}
};


/* O(n) time and O(1) space solution. */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == nullptr or headB == nullptr)
            return nullptr;

        ListNode *cursor_a = headA;
        ListNode *cursor_b = headB;
        bool restarted = false;
        while (true) {
            if (cursor_a == cursor_b)
                return cursor_a;
            if (cursor_a->next == nullptr) {
                if (restarted)
                    return nullptr;
                restarted = true;
                cursor_a = headB;
            } else {
                cursor_a = cursor_a->next;
            }
            if (cursor_b->next == nullptr) {
                cursor_b = headA;
            } else {
                cursor_b = cursor_b->next;
            }
        }
    }
};
