# กฤษฎาได้มาทำงานพิเศษในช่วงปิดเทอมที่ร้านหนังสือการ์ตูนแห่งหนึ่ง  โดยเจ้าของร้านได้สั่งให้กฤษฎามาจัดหนังสือการ์ตูน Attack On Titan เพื่อที่จะวางขายในวันรุ่งขึ้น  โดยกฤษฎาได้จัดหนังสือไปเรื่อยๆจนรู้สึกเบื่อหน่าย  จึงได้คิดเกมสนุกๆขึ้นมานั่นคือ  ในชั้นหนังสือจะมีแค่ด้านหน้ากับด้านหลังที่จะใส่หนังสือเข้าไปได้เรื่อยๆ และจะนำหนังสือออกได้แค่ด้านหน้า และใส่หนังสือเพิ่มได้แค่ด้านหลัง  โดยเมื่อเล่นเกมนี้ไปเรื่อยๆ กฤษฎาก็ลืมว่าในชั้นหนังสือนั้นมีหนังสือซ้ำกันหรือไม่  กฤษฎาเลยอยากให้คุณเขียนโปรแกรม Python เพื่อมาช่วยกฤษฎาคิดว่ามีหนังสือซ้ำกันในชั้นนั้นหรือไม่

# Input :
# จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นหนังสือที่มีอยู่ในชั้นอยู่แล้ว  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
# D                -> เป้นการนำหนังสือด้านหน้าออกจากชั้น
# E <value>   -> เป็นการนำหนังสือ Attack On Titan เล่มที่ value เข้าชั้นหนังสือจากด้านหลัง

class Queue:
    def __init__(self, list) -> None:
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def Enqueue(self, items):
        self.items.append(items)
        
    def Dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def getQueue(self):
        return self.items
    
list = input("Enter Input : ").split("/")
Q = Queue(list[0].split(" "))

list2 = list[1].split(",")

for i in list2:
    if i[0] == 'E': Q.Enqueue(i.split(" ")[1])
    if i[0] == 'D': Q.Dequeue()
    
t = []
temp = Q.getQueue()
isDup = 0

for x in temp:
    if x not in t:
        t.append(x)
    else:
        isDup = 1
        break
    
if isDup:
    print("Duplicate")
else:
    print("NO Duplicate")