# Chapter : 5 - item : 4 - VIM Text Editor

# กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor

# ***** อธิบาย Input 5 แบบ *****

# 1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป

# 2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

# 3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

# 4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

# 5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = Node('|')
        self._size = 1

    def __str__(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, str(self.head.data) 
        while cur.next != None:
            s += " " + str(cur.next.data)
            cur = cur.next
        return s

    def insert(self, data):
        node = Node(data)
        self._size += 1
        cur = self.head
        while cur.data != '|':
            cur = cur.next
        node.next = cur
        if cur.previous != None:
            cur.previous.next = node
        node.previous = cur.previous
        if cur.previous == None:
            self.head = node
        cur.previous = node

    def left(self):
        if self.head.data == '|':
            return
        cur = self.head
        while cur.next.data != '|':
            cur = cur.next
        node = cur.next
        if cur.previous != None:
            cur.previous.next = node
        cur.next = node.next
        node.next = cur
        node.previous = cur.previous
        if cur.previous != None:
            cur.previous = node
        if cur.next == None:
             self.tail = cur
        if node.previous == None:
             self.head = node

    def right(self):
        if self.tail.data == '|':
            return
        cur = self.head
        while cur.data != '|':
            cur = cur.next
        node = cur.next
        if cur.previous != None:
            cur.previous.next = node
        else:
            self.head = node
        cur.next = node.next
        if node.next != None:
            node.next.previous = cur
        else:
            self.tail = cur
        node.next = cur
        node.previous = cur.previous
        cur.previous = node

    def backSpace(self):
        if self.head.data == '|':
            return
        cur = self.head
        while cur.next.data != '|':
            cur = cur.next
        node = cur.next
        node.previous = cur.previous
        if cur.previous != None:
            node.previous.next = node
        else:
            self.head = node
            
    def delete(self):
        if self.tail.data == '|' or self.size() < 2:
            return
        cur = self.head
        while cur.data != '|':
            cur = cur.next
        node = cur.next
        cur.next = node.next
        if node.next != None:
            node.next.previous = cur
        else:
            self.tail = cur
            
    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self._size

if __name__ == '__main__':
    inp = input('Enter Input : ').split(',')
    L = LinkedList()
    for data in inp:
        data = data.split()
        if data[0] == 'I':
            L.insert(data[1])
        elif data[0] == 'L':
            L.left()
        elif data[0] == 'R':
            L.right()
        elif data[0] == 'B':
            L.backSpace()
        elif data[0] == 'D':
            L.delete()
    print(L)
        