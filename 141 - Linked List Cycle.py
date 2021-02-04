# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        temp = head
        reply = False
        if temp == None:
            return reply
        l = [temp]
        
        while(True):
            if(temp.next != None):
                temp = temp.next
                if(temp in l):
                    reply = True
                    break
                else:
                    l.append(temp)
            else: 
                break
        return reply
            
        