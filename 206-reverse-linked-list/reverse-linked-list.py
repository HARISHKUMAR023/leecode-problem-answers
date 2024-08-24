# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp=head
        # s=[]
        # while temp != None:
        #     s.append(temp.val)
        #     temp = temp.next 
        # p=head
        # while p != None:
        #     p.val=s.pop()
        #     p=p.next
        # return head
        temp = head 
        p = None 
        while temp != None :
            f= temp.next 
            temp.next = p
            p = temp 
            temp = f
        return p

            
           