# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        prev = None
        curr = head
        newHead = None
        while curr and curr.next:
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = curr
            if not newHead:
                newHead = tmp
            else:
                prev.next = tmp
            prev = curr
            curr = curr.next

        return newHead


# create a List as [1,2,3,4,5,6,7]
g = ListNode(7, next=None)
f = ListNode(6, next=g)
e = ListNode(5, next=f)
d = ListNode(4, next=e)
c = ListNode(3, next=d)
b = ListNode(2, next=c)
a = ListNode(1, next=b)

s = Solution()
print(s.swapPairs(a).val)
print(s.swapPairs(a).next.val)
print(s.swapPairs(a).next.next.val)
print(s.swapPairs(a).next.next.next)
