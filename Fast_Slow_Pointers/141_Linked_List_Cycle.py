# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        node = head
        nodes = []

        # node can be empty
        while node != None and node.next != None:
            if node.next in nodes:
                return True
            else:
                nodes.append(node)
                node = node.next
        return False


# create a List as [3,2,0,-4], pos = 1
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next = b
b.next = c
c.next = d
d.next = b

s = Solution()
print(s.hasCycle(a))
