# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode()
        current = dummy_head

        p1, p2 = l1, l2

        while p1 or p2 or carry:
            # Extract values or use 0 if the node is None
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            # Calculate sum and carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10

            # Update the result linked list
            current.next = ListNode(total_sum % 10)
            current = current.next

            # Move to the next nodes if available
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummy_head.next