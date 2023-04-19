class List :  
#Singly linked list ไม่มี header node
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

        
    def __init__(self,head = None):
                
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :# locating tail & find size
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        """ add at the end of list"""
        p = self.Node(data)
        if self.head == None:  # null list
            self.head = p
        else:
            t = self.head
            while t.next != None : 
                 t = t.next
            t.next = p     
        self.size += 1

    def add_first(self, data) :
        p = self.Node(data)
        p.next = self.head
        self.head = p
        self.size += 1

    def remove(self,data) :
        if self.head == None : return
        if self.head.data == data :
            self.head = self.head.next
            self.size -= 1
            return
        else :
            p = self.head
            while  p.next != None and p.next.data != data :
                p = p.next
        p.next = p.next.next
        self.size -= 1

    def removeHead(self) : # remove and retrun โหนดแรก

        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
            
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def removeTail(self) :
       if self.head == None : return
       if self.head.next == None :
           self.head = self.head.next
           self.size -= 1
           return 
       else :
            p = self.head
            while  p.next.next != None  :
                p = p.next
       p.next = p.next.next
       self.size -= 1
       return p.data

        
    def sizes(self) :
        return self.size

    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def search(self,data) :
        p = self.head
        while p != None :
            if p.data == data :
                return p
            p = p.next
        return None
        
    def insertAfter(self,data,i) :
        p = self.Node(data)
        q = self.nodeAt(i)
        p.next = q.next
        q.next = p

    def deleteAfter(self,i) :
        q = self.nodeAt(i)
        q.next = q.next.next

    def deleteAfterD(self,data) :
        if self.head == None : return
        if self.head.data == data and self.head.next == None:
            return
        p = self.head
        while p != None :
            if p.data == data and p.next != None :
                p.next = p.next.next
            p = p.next
                
        
    def isIn(self,data) :
        p = self.head
        while p != None :
            if p.data == data :
                return True
            p = p.next
        return False

    def reverse(self) :
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev

    def contentEquivalence(self,list2) :
        p = self.head
        q = list2.head
        if len(self) == len(list2) :
            while p != None :
                found = False
                q = list2.head
                while q != None :
                    #print(p.data," ",q.data)
                    if p.data == q.data :
                        found = True
                    q = q.next
                if found == False : return False
                p = p.next
            return True
        else :
            return False
        


l = List()
l.append('a')
l.append('b')
l.append('c')
l.append('d')
l.append('e')
l2 = List()
l2.append('a')
l2.append('d')
l2.append('c')
l2.append('b')
l2.append('e')
print(l.contentEquivalence(l2))


