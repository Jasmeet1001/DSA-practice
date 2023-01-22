class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def iterate(stack):
    return stack.__iterate__()

class Stack:
    '''
    Linked list implementation of a stack.
    '''
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def push(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.size += 1
            return
        
        ptr = self.head
        new_node.next = ptr
        self.head = new_node
        self.size += 1
        return

    def pop(self):
        if self.isEmpty():
            raise Exception("Pop from empty Stack")

        ptr = self.head
        self.head = ptr.next
        ptr.next = None
        self.size -= 1
        return

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack empty")
        
        return self.head.data

    def __iterate__(self):
        ptr = self.head
        for i in range(self.size):
            print(f"|{ptr.data}|")
            ptr = ptr.next


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)

    s.pop()
    s.pop()
    s.pop()

    print(s.peek())

    iterate(s)
