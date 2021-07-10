# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        nodes = [head]

        node = head.next

        while node != None:
            nodes.append(node)
            node = node.next

        l = len(nodes)
        return nodes[l // 2]


# create a List as [1,2,3,4,5]
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()
print(s.middleNode(a).val, s.middleNode(a).next.val)
