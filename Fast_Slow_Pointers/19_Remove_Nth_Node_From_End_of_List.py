class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        num = 0
        i = 0

        node = head
        while node != None:
            num += 1
            node = node.next

        loc = num - n

        node = head
        pre = None

        if loc == 0:
            return node.next
        else:
            while i < loc:
                pre = node
                node = node.next
                i += 1
            pre.next = node.next

        return head


# create a List as [1,2,3,4,5], n = 2
e = ListNode(5, next=None)
d = ListNode(4, next=e)
c = ListNode(3, next=d)
b = ListNode(2, next=c)
a = ListNode(1, next=b)

s = Solution()
print(s.removeNthFromEnd(a, 2).val)
print(s.removeNthFromEnd(a, 2).next.val)
print(s.removeNthFromEnd(a, 2).next.next.val)
print(s.removeNthFromEnd(a, 2).next.next.next.val)