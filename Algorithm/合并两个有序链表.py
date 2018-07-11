#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        result = ListNode(0)
        l = result
        if l1 is None:        #判断链表长度很重要
            return l2
        if l2 is None:
            return l1
        while l1 != None or l2 != None:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        return result.next
