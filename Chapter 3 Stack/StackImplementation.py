class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
                 
    def __str__(self):
        s = 'stack of' + str(self.size()) + 'items:'
        for ele in self.items:
            s += str(ele) + ''
        return s
    
    def push(self,i):
        self.items.append(i)
    
    def pop(self):  # remove & return อันบนสุด
       return self.items.pop()
    
    def peek(self): # return อันบนสุด
       return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    
