# ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบมากไปน้อย

# โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )

class LinkedList:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            if next is None:
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.Size = 0
            
    def __str__(self):
        s = ''
        p = self.head
        while p != None :
            s += str(p.data) + ' '
            p = p.next
        return s.rstrip(' ')

    def strAns(self):
        s = ''
        p = self.head
        while p != None:
            s += str(p.data) + ' -> '
            p = p.next
        return s.rstrip(' ->')
          
    def __len__(self):
        return self.Size         
            
    def isEmpty(self):
        return self.Size == 0
        
    def index(self, data):
        p = self.head
        for i in range(len(self)):
            if p.data == data:
                return i
            p = p.next
        return -1
            
    def isIn(self, data):
        return self.index(data) >= 0
    
    def nodeAt(self, i):
        p = self.head
        for j in range(0,i):
            p = p.next
        return p
    
    def append(self, data):
        if self.head is None:
          p = self.Node(data)
          self.head = p
          self.Size += 1
        else :
          self.insert(len(self), data)
    
    def insert(self, i, data):
        while i < 0:
            raise Exception()
        if i == 0:
            q = self.nodeAt(i)
            p = self.Node(data)
            self.head = p
            p.next = q
            self.Size += 1
            return
        elif i == len(self):
            q = self.nodeAt(i - 1)
            p = self.Node(data)
            q.next = p
            self.Size += 1
            return
        else:
            q = self.nodeAt(i - 1)
            p = self.Node(data)
            p.next = q.next
            q.next = p
            self.Size += 1
            return
    
    def deleteAfter(self, i):
        if self.Size > 0:
          q = self.nodeAt(i)
          p = q.next
          q.next = q.next.next
          self.Size -= 1
          return (i + 1, p)
    
    def delete(self, i):
        if i == 0 and self.Size > 0:
            p = self.head
            self.head = self.head.next
            self.Size -= 1
            return (i, p)
        else :
            out = self.deleteAfter(i-1)
            return out
        
    def remove(self, data):
        if self.isIn(data):
            i, p = self.delete(self.index(data))
            return p
        
    def addHead(self, data):
        if self.isEmpty():
          p = self.Node(data)
          self.head = p
          self.Size += 1
        else :
          p = self.Node(data, self.head)
          self.head = p
          self.Size += 1
    
    def size(self):
        return len(self)

    def pop(self, i = None):
        if i is None:
            q = self.nodeAt(len(self) - 2)
            p = q.next
            q.next = None
            self.Size -= 1
            return 'Success'
        else:
            if self.isEmpty() or i >= len(self):
                return 'Out of Range'
            else:
                q = self.nodeAt(i - 1)
                p = q.next
                try:
                    q.next = q.next.next
                except:
                    q.next = None
                self.Size -= 1
                return 'Success'
            
    def appendBySort(self, data: int):
        if self.head is None:
          p = self.Node(data)
          self.head = p
          self.Size += 1
          return
        p = self.head
        for i in range(len(self)):
            if p.data >= data:
                p = p.next
            else:
                self.insert(i, data)
                return
        self.append(data)
        
def cleanData(data: str):
    return data.replace('-', '')

def radixSort(data: LinkedList, round: int):
    print('------------------------------------------------------------')
    print('Round : {}'.format(round))
    isEnd = False
    outPutLinkList = LinkedList()
    R = LinkedList()
    data_copy = LinkedList()
    p = data.head
    for _ in range(data.size()):
        data_copy.append(p.data)
        p = p.next
    for i in range(10):
        p = data_copy.head
        for _ in range(data_copy.size()):
            if len(cleanData(str(p.data))) < round:
                R.appendBySort(p.data)
            else:
                if int(str(p.data)[round * -1]) == i:
                    R.appendBySort(p.data)
            p = p.next
        print('{} : {}'.format(i, R))
        if R.size() > 0:
            q = R.head
            for _ in range(R.size()):
                data_copy.remove(q.data)
                q = q.next
        if R.size() == data.size() and i == 0:
            isEnd = 1
            q = R.head
            for _ in range(R.size()):
                outPutLinkList.append(q.data)
                q = q.next
        R = LinkedList()
    return (isEnd, outPutLinkList)

inp = list(map(int, input('Enter Input : ').split()))
L = LinkedList()
old = LinkedList()
for i in inp:
    L.append(i)
    old.append(i)
i = 0
while 1:
    con, da = radixSort(L, i + 1)
    if con is 1:
        break
    i += 1
print('------------------------------------------------------------')
print(f'{i} Time(s)')
print('Before Radix Sort : ' + L.strAns())
print('After  Radix Sort : ' + da.strAns())