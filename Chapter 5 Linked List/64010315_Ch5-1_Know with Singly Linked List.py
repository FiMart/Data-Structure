# Chapter : 5 - item : 1 - รู้จักกับ Singly Linked List

# ให้เขียนคลาสของ Singly Linked List ซึ่งมีเมท็อดดังนี้
# 1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
# 2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
# 3. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
# 4. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
# 5. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
# 6. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
# 7. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
# 8. size           คืนค่าเป็นขนาดของ Linked List
# 9. pop            นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range

# โดยรูปแบบ Input มีดังนี้
# 1. append    ->  AP
# 2. addHead  ->  AH
# 3. search      ->  SE
# 4. index        ->   ID
# 5. size          ->   SI
# 6. pop          ->   PO

# โดยให้เพิ่มเติมจากส่วน #Code Here ของโปรแกรมต่อไปนี้ เพื่อให้สามารถแสดงผลได้ตามที่โจทย์กำหนด
# ********  ห้ามใช้ List ในการทำ Linked List เด็ดขาดถ้าหากพบจะถูกลดเป็น 0 คะแนน ********

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def __str__(self):
#         if self.isEmpty():
#             return "Empty"
#         cur, s = self.head, str(self.head.value) + " "
#         while cur.next != None:
#             s += str(cur.next.value) + " "
#             cur = cur.next
#         return s

#     def isEmpty(self):
#         return self.head == None

#     def append(self, item):
#         # Code Here

#     def addHead(self, item):
#         # Code Here

#     def search(self, item):
#         # Code Here

#     def index(self, item):
#         # Code Here

#     def size(self):
#         # Code Here

#     def pop(self, pos):
#         # Code Here

# L = LinkedList()
# inp = input('Enter Input : ').split(',')
# for i in inp:
#     if i[:2] == "AP":
#         L.append(i[3:])
#     elif i[:2] == "AH":
#         L.addHead(i[3:])
#     elif i[:2] == "SE":
#         print("{0} {1}".format(L.search(i[3:]), i[3:]))
#     elif i[:2] == "SI":
#         print("Linked List size = {0} : {1}".format(L.size(), L))
#     elif i[:2] == "ID":
#         print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
#     elif i[:2] == "PO":
#         before = "{}".format(L)
#         k = L.pop(int(i[3:]))
#         print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
# print("Linked List :", L)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        self._size += 1
        if self.isEmpty():
            self.head = Node(item)
            return
        node = self.head
        while (node.next != None):
            node = node.next
        node.next = Node(item)
        # print(self)

    def addHead(self, item):
        self._size += 1
        if self.isEmpty():
            self.head = Node(item)
            return
        node = self.head
        self.head = Node(item)
        self.head.next = node

    def search(self, item):
        node = self.head
        if self.isEmpty():
            return "Not Found"
        while node.next != None:
            if node.value == item:
                return "Found"
            node = node.next
        if node.value == item:
            return "Found"
        return "Not Found"

    def index(self, item):
        index = 0
        node = self.head
        if self.isEmpty():
            return -1
        if self.size() == 1:
            if node.value == item:
                return index
        while node.next != None:
            if node.value == item:
                return index
            node = node.next
            index += 1
        if node.value == item:
            return index
        return -1

    def size(self):
        return self._size

    def pop(self, pos):
        index = 0
        if pos >= self.size() or pos < 0:
            return "Out of Range"
        if pos == 0 and self.size() == 1:
            self.head = self.tail = None
        elif pos == 0:
            self.head.next.previous = None
            self.head = self.head.next
        else:
            node = self.head
            while index != pos - 1:
                index += 1
            node.next = node.next.next
        self._size -= 1
        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
