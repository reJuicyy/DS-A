# TODO

class Node:
    def __init__(self, data=0):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return False if self.head else True

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def remove_by_data(self, data):
        if self.is_empty(): 
            return
        
        if self.head.next is None:
            if self.head.data == data:
                self.head = self.tail = None
                return
        
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        
        curr = self.head
        while curr.next:
            if curr.data == data:
                prev.next = curr.next
                curr.next.prev = prev
                return
            prev = curr
            curr = curr.next
    
    def length(self):
        if self.is_empty():
            return 0
        
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def print_ll(self):
        if self.is_empty(): return
        
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next