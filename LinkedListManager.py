from aa import *

def main():
    print("Please choose one of the following options:")
    print("1. Insert an element")
    print("2. Search an element by data")
    print("3. Search an element by index")
    print("4. Print the linked list")
    n=int(input())
    ll=LinkedList()
    if n==1:
        print("Enter the element:")
        s=int(input())
        ll.insert(s)
    elif n==2:
        print("Enter the element you want to search:")
        data=int(input())
        ll.search(data)
    elif n==3:
        print("Enter the index you want to search:")
        index=int(input())
        ll.searchByIndex(index)
    elif n==4:
        ll.print()
