# Chapter : 5 - item : 5 - Radix Sort (น้อยไปมาก)

# ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบน้อยไปมาก

# โดยผลลัพธ์การทำ Radix Sort แสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบ , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )

# การเรียงเลขจำนวนลบ จะเรียงตรงข้ามกับเลขจำนวนบวก จึงควรแยก การเรียงตัวเลขบวก และเลขลบ ออกจากกัน

class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if len(self) == 0:
            return "-1"
        s = ""
        p = self.head
        while p != None:
            s += str(p.data) + " "
            p = p.next
        return s

    def reverse(self):
        if len(self) == 0:
            return "Empty"
        s = ""
        p = self.tail
        while p != None:
            s += str(p.data) + " "
            p = p.previous
        return s

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOf(self, data):
        p = self.head
        for i in range(len(self)):
            if p.data == data:
                return i
            p = p.next
        return -1

    def search(self, data):
        if (self.indexOf(data) != -1):
            return "Found "
        else:
            return "Not Found "

    def isIn(self, data):
        return self.indexOf(data) >= 0

    def nodeAt(self, i):
        p = self.head
        for j in range(0, i):
            p = p.next
        return p

    def dataAt(self, i):
        p = self.head
        for j in range(0, i):
            p = p.next
        return p.data

    def append(self, data):
        if self.head is None:
            p = self.Node(data)
            self.head = p
            self.tail = p
            self.next = None
            self.previous = None
            self.size += 1
        else:
            self.insertAfter(len(self)-1, data)

    def insertAfter(self, i, data):
        if len(self) == 0:
            self.addHead(data)
        else:
            if i < 0:
                if (-i > len(self)):
                    i = -1
                else:
                    i = len(self)+i-1
            if i >= len(self):
                i = len(self)-1
            if i == -1:
                self.addHead(data)
            else:
                q = self.nodeAt(i)
                p = self.Node(data)
                if len(self)-1 != i:
                    r = self.nodeAt(i+1)
                    r.previous = p

                p.next = q.next
                q.next = p
                p.previous = q

                if i == len(self)-1:
                    self.tail = p
                self.size += 1

    def deleteAfter(self, i):
        if i < 0:
            self.deleteHead()

        elif len(self) > 0:
            q = self.nodeAt(i)
        #   print("delete : "+str(q.data))
            q.next = q.next.next
            self.size -= 1

    def deleteHead(self):
        q = self.head.next
        # q.previous = None
        self.head = q
        self.size -= 1

    def pop(self, i):
        if len(self) > 0 and i < len(self):
            if i == 0 and len(self) > 0:
                self.head = self.head.next
                self.size -= 1
            else:
                self.deleteAfter(i-1)
            return "Success"
        else:
            return "Out of Range"

    def removeData(self, data):
        if self.isIn(data):
            self.deleteAfter(self.indexOf(data)-1)

    def addHead(self, data):
        if self.isEmpty():
            p = self.Node(data)
            self.head = p
            self.tail = p
            self.size += 1
        else:
            q = self.head
            p = self.Node(data)
            q.previous = p
            p.next = q
            self.head = p
            self.size += 1


inp = input("Enter Input : ").split(" ")
inp = [int(i) for i in inp]
num = []
numTemp = []
for i in range(10):
    num.append(LinkedList())
    numTemp.append(LinkedList())

max = max(inp)
maxDigit = len(str(max))

temp = inp[0]
chk = True
for i in inp:
    if temp == i:
        continue
    else:
        chk = False
if chk:
    maxDigit = -1

count = 1
countReal = 0
chk = False
for i in range(maxDigit):
    if not chk:
        print("------------------------------------------------------------")
        print("Round : "+str(count))

    if i == 0:
        for j in inp:
            if (j < 0):
                reminder = j % (10**count)
                num[-reminder].append(j)
        for j in inp:
            if j >= 0:
                reminder = j % (10**count)
                num[reminder].append(j)
    else:
        for j in range(10):
            for k in range(len(num[j])):
                numTemp[j].append(num[j].dataAt(0))
                num[j].deleteHead()

        for j in range(9, -1, -1):
            k = 0
            while k < len(numTemp[j]):
                # print(numTemp[j].dataAt(k))
                if numTemp[j].dataAt(k) < 0:
                    reminder = -numTemp[j].dataAt(0) % (10**count)
                    # print(str(reminder)+" "+str(10**(count-1)))
                    if reminder > (10**(count-1)):
                        reminder = str(reminder)
                        if (int(reminder) >= 0):
                            num[int(reminder[0])].append(numTemp[j].dataAt(k))
                            numTemp[j].deleteAfter(k-1)
                            k -= 1
                    else:
                        reminder = str(reminder)
                        num[0].append(numTemp[j].dataAt(k))
                        numTemp[j].deleteAfter(k-1)
                        k -= 1
                k += 1
                # if len(numTemp[j])<1:
                #     k-=1

        for j in range(10):
            for k in range(len(numTemp[j])):
                reminder = numTemp[j].dataAt(0) % (10**count)
                # print(reminder)
                if reminder >= (10**(count-1)):
                    reminder = str(reminder)
                    # print(reminder)
                    num[int(reminder[0])].append(numTemp[j].dataAt(0))
                    numTemp[j].deleteHead()
                else:
                    num[0].append(numTemp[j].dataAt(0))
                    numTemp[j].deleteHead()

    if not chk:
        for j in range(10):
            li = list(num[j].__str__().split(" "))
            li.pop(-1)
            for k in range(len(li)):
                li[k] = int(li[k])

            print(str(j)+" :", end=" ")
            for k in li:
                print(str(k), end=" ")
            print("")
            if len(li) == len(inp) and j == 0:
                chk = True
                countReal = count+1
    count += 1

print("------------------------------------------------------------")
print(str(countReal+3)+" Time(s)")
print("Before Radix Sort :", end=" ")
for i in range(len(inp)):
    print(inp[i], end=" ")
    if i != len(inp)-1:
        print("->", end=" ")
print("")
print("After  Radix Sort :", end=" ")
for i in range(len(num[0])):
    print(num[0].dataAt(i), end=" ")
    if i != len(num[0])-1:
        print("->", end=" ")
