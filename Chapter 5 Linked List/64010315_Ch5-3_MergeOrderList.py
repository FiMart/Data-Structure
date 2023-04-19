# Chapter: 5 - item: 3 - MergeOrderList

# จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้

# createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist

# printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว

# mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว

# ****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****

# ****ห้ามสร้าง Class LinkList****


# class node:
#     def __init__(self, data, next=None):
#         ### Code Here ###

#     def __str__(self):
#         ### Code Here ###


# def createList(l=[]):
#     ### Code Here ###


# def printList(H):
#     ### Code Here ###


# def mergeOrderesList(p, q):
#     ### Code Here ###

#     #################### FIX comand ####################
#     # input only a number save in L1,L2
# LL1 = createList(L1)
# LL2 = createList(L2)
# print('LL1 : ', end='')
# printList(LL1)
# print('LL2 : ', end='')
# printList(LL2)
# m = mergeOrderesList(LL1, LL2)
# print('Merge Result : ', end='')
# printList(m)

class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    p = node(l[0])
    h = p
    for i in range(1, len(l)):
        q = node(l[i])
        p.next = q
        p = q
    return h

def printList(H):
    x = ''
    while H is not None:
        x += str(H) + ' '
        H = H.next
    print(x)

def mergeOrderesList(p,q):
    m = None
    if p.data <= q.data:
        m = node(p.data)
        p = p.next
    else:
        m = node(q.data)
        q = q.next
    h = m
    while p is not None and q is not None:
        if p.data <= q.data:
            m.next = p
            m = p
            p = p.next
        else:
            m.next = q
            m = q
            q = q.next
    while p is not None:
        m.next = p
        m = p
        p = p.next
    while q is not None:
        m.next = q
        m = q
        q = q.next
    return h

#################### FIX comand ####################   
# input only a number save in L1,L2
L1, L2 = input('Enter 2 Lists : ').split()
L1 = list(map(int, L1.split(',')))
L2 = list(map(int, L2.split(',')))
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)