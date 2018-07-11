# -*- coding: utf-8 -*
class ListNode(object):
    def __init__(self,val,p=None):
        self.data = val
        self.next = p

class list(object):
    def initlist(self,data):
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

class Solution():
    def swapPairs(self, head):
        if head==None or head.next==None:
            return head
        else:
            start=ListNode(0)
            start.next=head
            p=start
            q=start.next
            while q!=None and q.next!=None:
                p.next=q.next
                q.next=p.next.next
                p.next.next=q
                p=q
                q=q.next
            return start.next
    def shuchu(self,head):
        p=head
        while p!=None:
            print p.data
            p=p.next
s = Solution()
l=list()
l.initlist([])
p=s.swapPairs(l.head)
s.shuchu(p)

