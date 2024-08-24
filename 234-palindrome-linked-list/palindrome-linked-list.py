# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        my=[]
        p=head
        while  p != None:
            my.append(p.val)
            p=p.next
        if my == my[::-1]:
            return True 
        else:
            return False
