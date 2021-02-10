# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node = head
        if(node==None or node.next==None):
            return False
        flag=False
        l=[]
        while(node not in l):
            l.append(node)
            if(node.next!=None):
                node = node.next
            else:
                break
        else:
            flag = True

        return flag
        