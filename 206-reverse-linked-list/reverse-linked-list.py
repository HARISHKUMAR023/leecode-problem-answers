# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        s=[]
        while temp != None:
            s.append(temp.val)
            temp = temp.next 
        p=head
        while p != None:
            p.val=s.pop()
            p=p.next
        return head
            
            # # print(p.val)
            # if p.next != None:
            #      p = p.next 
            # else:
            #      head = p.next
            #      break
        
            
    