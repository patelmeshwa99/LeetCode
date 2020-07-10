/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        if(head==null){
            return head;
        }
        
        Node tail = head;
        while(tail.next != null){
            tail = tail.next;
        }
        
        Node current = head;
        while(current != null){
            if(current.child != null){
                if(current.next != null){
                    Node next_one = current.next;
                    current.next = current.child;
                    current.next.prev = current;
                    Node temp = current.child;
                    while(temp.next != null){
                        temp = temp.next;
                    }
                    temp.next = next_one;
                    temp.next.prev = temp;                
                    current.child=null;
                }
                else
                {
                    current.next = current.child;
                    current.next.prev = current;
                    current.child=null;

                }
            }
            current = current.next;
        }
        return head;
    }
}