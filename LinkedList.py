class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList():
    def __init__(self):
        self.head=None

    def insert(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    # def  remove(self,data):
    #     if self.

    def print(self):
        itr=self.head
        l=""
        while itr.next:
            l+=str(itr.data)+" "
            itr=itr.next
        l+=str(itr.data)
        print(l)

    def printByHead(self,head):
        itr=head
        while itr:
            print(itr.value," ",end='')
            itr=itr.next

    def search(self,data):
        itr=self.head
        i=0
        counter=0
        while True:
            if itr.data==data:
                i=1
                print("Element found at position",counter)
                break
            itr=itr.next
            counter+=1
        if i==0:
            print("Element not found!!")

    def deleteLastItem(self):
        itr=self.head
        while itr.next:
            if itr.next.next is None:
                break
            itr=itr.next
        itr.next = None

    def delete(self,data):
        itr=self.head
        while True:
            if itr.next is None:
                break
            if itr.data==data:
                itr.data=itr.next.data
                itr.next=itr.next.next
            itr=itr.next

    def searchByIndex(self,index):
        counter=0
        i=0
        itr=self.head
        while itr.next:
            if counter==index:
                i=1
                print("Element at index is {}".format(itr.data))
                break
            itr=itr.next
            counter+=1
        if i==0:
            print("Element not found!!!")

    def modifyByIndex(self,index,val):
        counter=0
        itr=self.head
        # itr.next
        while True:
            if counter==index:
                itr.data=val
                break
            itr=itr.next
            counter+=1

    def reverse(self,head):
        curr=head
        prev=head
        tmp=head.next
        curr.next=None
        while tmp:
            curr=tmp
            tmp=tmp.next

            curr.next=prev
            prev=curr
        head=curr
        return head

a=LinkedList()
n=int(input())
l=list(map(int,input().split()))
for i in range (n):
    a.insert(l[i])
a.print()
hn=a.reverse(a.head)
a.printByHead(hn)
