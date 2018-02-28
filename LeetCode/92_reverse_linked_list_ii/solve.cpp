/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
#include <stack>

class Solution {
public:
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        struct ListNode super_head = {0};
        super_head.next = head;

        // traverse to previous node of m
        struct ListNode *prev_m = &super_head;
        int idx = 0;
        while (idx != m - 1) {
            prev_m = prev_m->next;
            ++idx;
        }

        // push [m, n] nodes into stack
        std::stack<ListNode *> stack;
        struct ListNode *next_n = prev_m->next;
        idx = m;
        while (idx != n + 1) {
            stack.push(next_n);
            next_n = next_n->next;
            ++idx;
        }

        // revesing
        while (stack.empty() == false) {
            prev_m->next = stack.top();
            stack.pop();
            prev_m = prev_m->next;
        }
        prev_m->next = next_n;
        return super_head.next;
    }
};
