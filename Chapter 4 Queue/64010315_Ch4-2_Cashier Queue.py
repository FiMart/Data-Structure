# Chapter : 4 - item : 2 - แถวคอย

# # จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

# # โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

# # แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

# # แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

# # ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

# # จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2]

class Queue:
    def __init__(self,lst = None):
        if lst is None:
            self.lst = []
        else:
            self.lst = lst

    def enqueue(self, item):
        self.lst.append(item)
        
    def dequeue(self):
        return self.lst.pop(0)
    
    def isEmpty(self):
        return len(self.lst) == 0
    
    def size(self):
        return len(self.lst)
    
cm = Queue()
c1 = Queue()
c2 = Queue()
w,t = input("Enter people and time : ").split()
for i in w:
    cm.enqueue(i)
c = 0
for j in range(int(t)):
    if j>0 and j%3 == 0 and not c1.isEmpty():
            c1.dequeue()
    if c>0 and c%2 == 0 and not c2.isEmpty():
            c2.dequeue()
    if cm.size()>0 :
        if c1.size() < 5:
            c1.enqueue(cm.dequeue())
        else:
            c2.enqueue(cm.dequeue())
            if c2.size() == 1:
                c = 0 
    c += 1      
    print(f'{j+1} {cm.lst} {c1.lst} {c2.lst}')