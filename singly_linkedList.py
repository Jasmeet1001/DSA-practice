class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        ptr = self.head
        while(ptr.next != None):
            ptr = ptr.next
        ptr.next = Node(data)
        return

    def insertFront(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        ptr = self.head
        new_node = Node(data)
        new_node.next = ptr
        self.head = new_node
        return 
    
    def insertAt(self, position, data):
        if position == 1:
            self.insertFront(data)
            return
        if self.head == None:
            self.insertEnd(data)
            return
        ptr = self.head
        for i in range(position - 2):
            ptr = ptr.next
        new_node = Node(data)
        new_node.next = ptr.next
        ptr.next = new_node
        return

    def removeEnd(self):
        if self.head == None:
            raise Exception("Cannot Remove from empty linked list")
        ptr = self.head
        while(ptr.next.next != None):
            ptr = ptr.next
        ptr.next = None

    def removeFront(self):
        if self.head == None:
            raise Exception("Cannot Remove from empty linked list")
        self.head = self.head.next

    def removeNode(self, data):
        if self.head == None:
            raise Exception("Cannot Remove from empty linked list")
        ptr = self.head
        ptr1 = self.head.next
        while(ptr1.next != None):
            if (ptr1.data == data):
                # ptr1 = ptr1.next
                break
            ptr = ptr.next
            ptr1 = ptr1.next
        ptr.next = ptr1.next
        return
    
    def removeAt(self, position):
        if self.head == None:
            raise Exception("Cannot Remove from empty linked list")
        ptr = self.head
        ptr1 = self.head.next
        for i in range(position-2):
            if(ptr1.next != None):
                ptr = ptr.next
                ptr1 = ptr1.next
        ptr.next = ptr1.next
        return

if __name__ == "__main__":

    llist = SLinkedList()
    llist.insertEnd(10)
    llist.insertEnd(20)
    llist.insertEnd(50)
    llist.insertEnd(60)
    llist.insertEnd(70)
    llist.insertFront(30)
    llist.insertAt(2, 4)

    llist.removeEnd()
    llist.removeFront()
    llist.removeAt(4)
    llist.removeNode(20)

    trav = llist.head
    while(trav != None):
        print(trav.data)
        trav = trav.next