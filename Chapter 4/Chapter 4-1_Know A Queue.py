# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา



# E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผล Size ปัจจุบันของ QUEUE

# D                 ให้ทำการแสดงผลของvalueที่อยู่หน้าสุดและindexของvalueนั้นจากนั้นทำการ De_QUEUE ถ้าหากไม่มี value อยู่ใน Queue ให้แสดงผลเป็น  -1

# *** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def push(self, items):
        self.items.append(items)
        
    def pop(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def value(self):
        return self.items
    
    def isEmpty(self):
        return self.items == []
    
    def front(self):
        return self.items[0]
    
a = [i for i in input("Enter Input : ").split(',')]
s = Queue()

for items in a:
    x = items.split(' ')
    if x[0] == "E":
        s.push(x[1])
        print(s.size())
    elif x[0] == "D":
        if s.isEmpty():
         print("-1")
        else:
            print(f'{s.front()} 0')
            s.pop()
            
if s.isEmpty():
    print("Empty")
else:
    print(str(s.items).replace("[",'').replace("]",'').replace("\'",'').replace(",",''))