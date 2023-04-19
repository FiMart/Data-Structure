class Queue:
    def __init__(self,list = None):
        if list is None:
            self.items = []
        else:
            self.items = list
    
    def enQueue(self,i):
        self.items.append(i)    # insert ที่ท้าย list
    
    def deQueue(self):
        return self.items.pop(0)    # pop out index 0
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)