class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        super_head = ListNode(0)
        super_head.next = head

        # traverse to previous node of m
        prev_m = super_head
        idx = 0
        while idx != m - 1:
            prev_m = prev_m.next
            idx += 1

        # push [m, n] nodes into stack (next_n will get the node right after n)
        stack = list()
        next_n = prev_m.next
        idx = m
        while idx != n + 1:
            stack.append(next_n)
            next_n = next_n.next
            idx += 1

        # revesing
        while len(stack) != 0:
            prev_m.next = stack.pop()
            prev_m = prev_m.next
        prev_m.next = next_n

        return super_head.next
