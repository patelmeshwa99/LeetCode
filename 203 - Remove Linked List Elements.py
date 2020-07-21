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
    public ListNode removeElements(ListNode head, int val) {
        ListNode temp = head, prev = null; 
        while(temp!=null)
        {
            if(prev==null)
            {
                head=temp;
            }
            if(temp.val==val && temp.next==null)
            {
                if(head==temp){
                    head=temp.next;
                    return head;
                }
                prev.next=null;
            }
            if(temp.val==val)
            {
                if(head==temp)
                {
                    prev=temp;
                    temp=temp.next;
                    prev=null;
                }
                else
                {
                    temp=temp.next;
                    prev.next=temp;
                }
            }
            else
            {
                prev=temp;
                temp=temp.next;
            }
        }
        return head;    
    }
}