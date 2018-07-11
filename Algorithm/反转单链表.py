# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:        #判断链表长度很重要
            return head
        p = head
        q = p.next
        p.next = None
        while q.next!= None:
            r = q.next
            q.next = p
            p = q
            q = r
        q.next = p
        return q
