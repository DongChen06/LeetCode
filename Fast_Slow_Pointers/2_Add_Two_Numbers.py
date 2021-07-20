# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2

        val1 = 0
        val2 = 0

        index1 = 0
        index2 = 0

        # calculate the values of the two NodeLists
        while node1 != None:
            val1 += node1.val * (10 ** index1)
            index1 += 1
            node1 = node1.next

        while node2 != None:
            val2 += node2.val * (10 ** index2)
            index2 += 1
            node2 = node2.next

        val_new = val1 + val2

        # create a list nodes
        # out = [ListNode()] * len(str(val_new))  # TODO: this will cause isses as it's a copy of class.
        out = [ListNode() for i in range(len(str(val_new)))]
        out.append(None)
        for i in range(len(str(val_new))):
            out[i].val = int(str(val_new)[len(str(val_new))-1-i])
            out[i].next = out[i+1]
        return out[0]


# create a List as [2,4,3]
c = ListNode(3, next=None)
b = ListNode(4, next=c)
a = ListNode(2, next=b)

# [5,6,4]
c1 = ListNode(4, next=None)
b1 = ListNode(6, next=c1)
a1 = ListNode(5, next=b1)


s = Solution()
print(s.addTwoNumbers(a, a1).val)
print(s.addTwoNumbers(a, a1).next.val)
print(s.addTwoNumbers(a, a1).next.next.val)