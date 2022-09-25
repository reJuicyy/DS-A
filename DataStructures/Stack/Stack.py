# TODO

class Stack:
    def __init__(self) -> None:
        self.stack = []
        
    def is_empty(self):
        return self.stack == []
    
    def print(self):
        print(self.queue)
        
    def size(self):
        return len(self.queue)
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()