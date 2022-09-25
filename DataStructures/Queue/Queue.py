# TODO

class Queue:
    def __init__(self) -> None:
        self.queue = []
        
    def is_empty(self):
        return self.queue == []
    
    def print(self):
        print(self.queue)
    
    def size(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)