class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        pre_node = None
        curr_node = head
        next_node = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = pre_node
            pre_node = curr_node
            curr_node = next_node

        return pre_node


# create a List as [1,2,3,4]
d = ListNode(4, next=None)
c = ListNode(3, next=d)
b = ListNode(2, next=c)
a = ListNode(1, next=b)

s = Solution()
print(s.reverseList(a).val)
print(s.reverseList(a).next.val)
print(s.reverseList(a).next.next.val)
print(s.reverseList(a).next.next.next.val)
