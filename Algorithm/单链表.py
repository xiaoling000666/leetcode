#-*-coding:utf-8-*-
class Node(object):
    def __init__(self, data, pnext = None):
        self.data = data
        self.next = pnext
class LinkList(object):
    #初始化建立单链表
    def initlist(self, data):
        head = Node(data[0])
        p = head
        for i in range(1, len(data)):
            p.next = Node(data[i])
            p = p.next
        return head
    #统计中节点的个数
    # def getlistlength(self,head):
    #     p=head
    #     sum=0
    #     while p != None:
    #         sum=sum+1
    #         p=p.next
    #     return sum
    # def getlistlength(self, p, sum):
    #     if p == None:
    #         return 0
    #     else:
    #         return self.getlistlength(p.next)
    #反转单链表
    def reverse(self,list,head):
        p = head
        q = p.next
        p.next = None
        while q != None:
            r = q.next
            q.next = p
            p = q
            q = r
        return p
    #打印单链表
    def printlist(self, head):
        p = head
        while p != None:
            print p.data
            p = p.next
l = LinkList()
head = l.initlist([1,2,3,4,5])
p = l.reverse(list,head)
l.printlist(p)
#sum=l.getlistlength(head,0)
#print(sum)