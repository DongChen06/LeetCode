class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel_head = ListNode(0, head)
        pred = sentinel_head

        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                pred.next = head.next
            else:
                ## important
                pred = pred.next

            head = head.next
        return sentinel_head.next


# create a List as [1,2,3,3,4,4,5]
g = ListNode(5, next=None)
f = ListNode(4, next=g)
e = ListNode(4, next=f)
d = ListNode(3, next=e)
c = ListNode(3, next=d)
b = ListNode(2, next=c)
a = ListNode(1, next=b)

s = Solution()
print(s.deleteDuplicates(a).val)
print(s.deleteDuplicates(a).next.val)
print(s.deleteDuplicates(a).next.next.val)
print(s.deleteDuplicates(a).next.next.next)