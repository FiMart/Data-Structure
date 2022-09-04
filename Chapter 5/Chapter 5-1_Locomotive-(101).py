# มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่

# แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก

# โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้

# ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ

# เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

# เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list)

class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.siz = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cursor, c = self.head, str(self.head.value) + " <- "
        while cursor.next.next != None:
            c += str(cursor.next.value) + " <- "
            cursor = cursor.next
        c += str(cursor.next.value)
        return c

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head is None:
            self.head = self.Node(item)
            self.siz += 1
        else:
            a = self.head
            for i in range(0,self.siz-1):
                a = a.next
            b = self.Node(item)
            a.next = b
            self.siz += 1

    def appendNode(self,node):
        a = self.head
        while(a.next != None):
            a = a.next
        a.next = node
        self.siz += 1

    def addHead(self, item):
        if self.isEmpty():
            a = self.Node(item)
            self.head = a
            self.siz += 1
        else:
            a = self.Node(item)
            a.next = self.head
            self.head = a
            self.siz += 1

    def search(self, item):
        if self.index(item)>=0:
            return "Found"
        else:
            return "Not Found"

    def index(self, item):
        a = self.head
        for i in range(self.size()):
            if a.value == item:
                return i
            a = a.next
        return -1

    def NodeAt(self,index):
        a = self.head
        for i in range(index):
            a = a.next
        return a

    def size(self):
        return self.siz

    def pop(self, position):
        if position < 0 or position >= self.siz:
            return "Out of Range"
        if position == 0 and self.siz > 0:
            self.head = self.head.next
            self.siz -= 1
            return "Success"
        else:
            a = self.head
            for i in range(0,position-1):
                a = a.next 
            a.next =a.next.next
            self.siz -= 1
            return "Success"
    
    def reverse(self):
        previous = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
 
    def returnhead(self):
        return self.head

    def changehead(self,hv):
        self.head = hv

print(" *** Locomotive ***")
inp = input("Enter Input : ").split()
LL = LinkedList()
for i in inp:
    LL.append(i)
print("Before : " + str(LL))
temphead = LL.returnhead()
siz = LL.size()
if int(temphead.value) != 0:
    for i in range(siz):
        if int(LL.NodeAt(i).next.value) == 0 :
            hv = LL.NodeAt(i).next
            LL.NodeAt(i).next = None
            LL.changehead(hv)
            break
    LL.appendNode(temphead)
print("After : " + str(LL))