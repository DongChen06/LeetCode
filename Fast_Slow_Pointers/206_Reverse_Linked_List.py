class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def reverseList(self, head):
#         pre_node = None
#         curr_node = head
#         next_node = None
#
#         while curr_node:
#             next_node = curr_node.next
#             curr_node.next = pre_node
#             pre_node = curr_node
#             curr_node = next_node
#
#         return pre_node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # iterative O(N), O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = None, head

        while curr:
            curr.next, pre, curr = pre, curr, curr.next
        return pre


class Solution:
    # recursion O(N), O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(node, pre=None):
            if not node:
                return pre
            n = node.next
            node.next = pre
            return recursion(n, node)

        return recursion(head)


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
