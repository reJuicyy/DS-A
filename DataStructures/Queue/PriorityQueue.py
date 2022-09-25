# TODO

class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
        
    def is_empty(self):
        return self.queue == []
    
    def size(self):
        return len(self.queue)
    
    def heapify(self, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < self.size() and self.queue[i] < self.queue[l]:
            largest = l
            
        if r < self.size() and self.queue[largest] < self.queue[r]:
            largest = r
            
        if largest != i:
            self.queue[i], self.queue[largest] = self.queue[largest], self.queue[i]
            self.heapify(largest)
    
    def insert(self, item):
        if self.is_empty():
            self.queue.append(item)
        else:
            self.queue.append(item)
            for i in range((self.size() // 2) - 1, -1, -1):
                self.heapify(i)
                
    def delete(self, item):
        for i in range(0, self.size()):
            if item == self.queue[i]:
                break
            
        self.queue[i], self.queue[self.size() - 1] = self.queue[self.size() - 1], self.queue[i]
        
        self.queue.remove(self.size() - 1)
        
        for i in range((self.size() // 2) - 1, -1, -1):
            self.heapify(i)