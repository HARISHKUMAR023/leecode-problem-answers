/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode temp = head;
        ListNode p = null;
        
        while (temp != null) {
            ListNode f = temp.next;  
            temp.next = p;           
            p = temp;                
            temp = f;               
        }
        
        return p;
    }
}