class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def insertEnd(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            return
        ptr = self.head
        while(ptr.next != None):
            ptr = ptr.next
        
        ptr.next = new_node
        new_node.prev = ptr

    def insertFront(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return

    def insertAt(self, position, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            return
        if position == 1:
            self.insertFront(data)
        
        ptr = self.head
        for i in range(position-2):
            if(ptr.next != None):
                ptr = ptr.next
        new_node.next = ptr.next
        new_node.prev = ptr
        ptr.next.prev = new_node
        ptr.next = new_node

    def removeEnd(self):
        if self.isEmpty():
            raise Exception("Cannot remove from empty linked list")
        
        ptr = self.head
        while(ptr.next.next != None):
            ptr = ptr.next
        
        ptr.next = None
        return

    def removeFront(self):
        if self.isEmpty():
            raise Exception("Cannot remove from empty linked list")

        self.head = self.head.next
        self.head.prev = None
        return

    def removeAt(self, position):
        if self.isEmpty():
            raise Exception("Cannot remove from empty linked list")
        
        ptr = self.head
        ptr1 = self.head.next
        for i in range(position-2):
            if(ptr1.next != None):
                ptr = ptr.next
                ptr1 = ptr1.next
        ptr.next = ptr1.next
        ptr1.next.prev = ptr
        return

    def removeNode(self, data):
        if self.isEmpty():
            raise Exception("Cannot remove from empty linked list")
        
        ptr = self.head
        ptr1 = self.head.next
        while(ptr1.next != None):
            if(ptr1.data == data):
                # ptr1 = ptr1.next
                break
            ptr = ptr.next
            ptr1 = ptr1.next
        
        if (ptr1.next == None):
            self.removeEnd()
            return

        ptr.next = ptr1.next
        ptr1.next.prev = ptr
        


if __name__ == "__main__":
    llist = DLinkedList()
    llist.insertEnd(10)
    llist.insertEnd(20)
    llist.insertEnd(30)
    llist.insertEnd(40)
    llist.insertEnd(50)
    llist.insertEnd(60)

    llist.insertFront(200)
    llist.insertAt(2, 5)

    #Forward traversal
    trav0 = llist.head
    while(trav0 != None):
        print(trav0.data, end=', ')
        trav0 = trav0.next
    print()

    llist.removeEnd()
    llist.removeFront()
    llist.removeAt(4)
    llist.removeNode(20)

    #Forward traversal
    trav = llist.head
    while(trav != None):
        print(trav.data, end=', ')
        trav = trav.next
    print()
    
    #Backward Traversal
    trav1 = llist.head
    while(trav1.next != None):
        trav1 = trav1.next
    print(trav1.data, end=', ')
    while(trav1.prev != None):
        print(trav1.prev.data, end=', ')
        trav1 = trav1.prev
