# -*- coding: utf-8 -*
class Node(object):
    def __init__(self,val,p=None):
        self.data = val
        self.next = p

class list(object):
    def __init__(self):                 #头节点为0
        self.head = 0
    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

class Solution():
    def removeNthFromEnd(self, head, n):
        p=head
        q=head
        while n!=0:
            q=q.next
            n=n-1
            if q==None :
                return head.next
        while q.next!=None:
            p=p.next
            q=q.next
        r=p.next
        p.next=r.next
        return head
    def shuchu(self,head):
        p=head
        while p!=None:
            print p.data
            p=p.next
s = Solution()
l=list()
l.initlist([1,2,3,4])
p=s.removeNthFromEnd(l.head,3)
s.shuchu(p)

