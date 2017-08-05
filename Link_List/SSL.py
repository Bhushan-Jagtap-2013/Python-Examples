class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next

if __name__ == '__main__':
    ll = SinglyLinkList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Create LL

    ll.head.next = second
    second.next = third

    # Print list
    ll.printList()
