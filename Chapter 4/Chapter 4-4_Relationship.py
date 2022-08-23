# สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
# ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

# กิจกรรม                                       สถานที่
# 0 = กินข้าว(Eat)                           0 = ร้านอาหาร(Res.)
# 1 = เล่นเกม(Game)                      1 = ห้องเรียน(ClassR.)
# 2 = ทำโจทย์ datastruc(Learn)      2 = ห้างสรรพสินค้า(SuperM.)
# 3 = ดูหนัง(Movie)                        3 = บ้าน(Home)

# โดยการรับ Input จะประกอบด้วย

# กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,

# เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร 
       # วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
# จะได้ว่า 0:0 2:0,1:3 3:2

# ***มีการคิดคะแนนดังนี้***

# ·       กิจกรรมเดียวกันแต่คนละสถานที่         +1

# ·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน    +2

# ·       กิจกรรมเดียวกันและสถานที่เดียวกัน    +4

# ·       ไม่เหมือนกันเลย                                   - 5

# หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน

# โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่าง

class Queue:
       def __init__(self):
              self.items = []
              
       def Enqueue(self, items):
            self.items.append(items)
       
       def Dequeue(self):
              if not self.isEmpty():
                     return self.items.pop(0)
              return -1
       
       def isEmpty(self):
              return self.size() == 0
       
       def size(self):
              return len(self.items)
       
       def Queue(self):
              return self.items
       
       def __str__(self):
              return str(self.items)
       
       def Value(self, value):
              return self.items[value]
       
       def isFull(self):
              return self.items.full()
       
def Act(str):
    if str == '0':
        return 'Eat'
    elif str == '1':
        return 'Game'
    elif str == '2':
        return 'Learn'
    elif str == '3':
        return 'Movie'

def Locate(str):
    if str == '0':
        return 'Res.'
    elif str == '1':
        return 'ClassR.'
    elif str == '2':
        return 'SuperM.'
    elif str == '3':
        return 'Home'
 
inp = input("Enter Input : ").split(",")
myQ = Queue()
yourQ = Queue()
myAct = Queue()
yourAct = Queue()

score = 0

for i in inp:
    l = i.split(' ')
    my = str(l[0]).split(":")
    your = str(l[1]).split(":")
    if my == your:
        score += 4
    elif my[1] == your[1]:
        score += 2
    elif my[0] == your[0]:
        score += 1
    else:
        score -= 5

    myQ.Enqueue(l[0])
    yourQ.Enqueue(l[-1])
    a = Act(my[0]) + ':' + Locate(my[1])
    myAct.Enqueue(a)
    a = Act(your[0]) + ':' + Locate(your[1])
    yourAct.Enqueue(a)

print("My   Queue = " + str(myQ).replace("\'",'').replace("[",'').replace("]",''))
print("Your Queue = " + str(yourQ).replace("\'",'').replace("[",'').replace("]",''))
print("My   Activity:Location = " + str(myAct).replace("\'",'').replace("[",'').replace("]",''))
print("Your Activity:Location = " + str(yourAct).replace("\'",'').replace("[",'').replace("]",''))

if score >= 7:
    print("Yes! You're my love! : Score is " + str(score) + '.')
elif score > 0:
    print("Umm.. It's complicated relationship! : Score is " + str(score) + '.')
else:
    print("No! We're just friends. : Score is " + str(score) + '.')

       
