class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,data):
        self.items.append(data)
    
    def dequeue(self,data):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print("Empty Queue")
            return -1
    
    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            print("Empty Queue")
            return -1
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    