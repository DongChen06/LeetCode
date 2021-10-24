# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # O(n), O(1): [1,2,3,4,5,6,7] --> [1,2,3,4] + [7,6,5]

        # step1: find the middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step2: reverse the second half
        pre, curr = None, slow.next
        while curr:
            curr.next, pre, curr = pre, curr, curr.next
        slow.next = None

        # merge the two linked lists
        head1, head2 = head, pre
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt

        return head