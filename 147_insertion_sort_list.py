# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        start = ListNode()
        start.next = head
        temp = start
        node = head        
        while node and node.next:
            
            if (node.val >= node.next.val):
                
                while temp.next:
                    if temp.next.val >= node.next.val:
                        p = temp.next
                        temp.next = node.next
                        node.next = node.next.next
                        temp.next.next = p
                        temp = start
                    else:
                        temp = temp.next
                
            else:
                node = node.next
        
        return start.next

# create a Node_List [4,3,2,1]
a3 = ListNode(1)  
a2 = ListNode(2, a3)  
a1 = ListNode(3, a2)  
a0 = ListNode(4, a1)  

answer = Solution()
l = answer.insertionSortList(a0)
print(l.val)
print(l.next.val)
print(l.next.next.val)
print(l.next.next.next.val)
