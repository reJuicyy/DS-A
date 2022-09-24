# TODO

class Node:
    def __init__(self, data=0) -> None:
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def is_empty(self):
        return False if self.head else True
    
    def append(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        
    def remove_by_data(self, data):
        if self.is_empty():
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        curr = self.head
        while curr:
            if curr.data == data:
                if curr.next is None:
                    prev.next = None
                elif curr.next is not None:
                    prev.next = curr.next
                    curr.next = None
                else:
                    return
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
    
    def print_ll(self, inline=True):
        if self.is_empty():
            return
        
        curr = self.head
        while curr:
            if inline:
                print(curr.data, end=" ")
            else:
                print(curr.data)
            curr = curr.next