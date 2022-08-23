# ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

# การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

# ***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

# *** สามารถสร้างได้มากกว่า 1 stack ***

class Stack:
    def __init__(self,list = None):
        if list == None:
            self.list = []
        else:
            self.items = list
            
    def pop(self):
        return self.items.pop(len(self.items)-1)
    
    def push(self,items):
        self.items.append(items)
        
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
        
print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m), int(n)
i = [x for x in s.split(',')]

if i[0] == str(0): 
    i = []

S = Stack()
S.items = i

if o == 'arrive':
    if S.size() == m:
        print("car " + str(n) + " cannot arrive : Soi Full")
    elif str(n) not in i:
        print("car " + str(n) + " arrive! : Add Car " + str(n))
        S.push(str(n))
    elif str(n) in i:
        print("car " + str(n) + " already in soi")
    
if o == 'depart':
    if S.isEmpty():
        print("car " + str(n) + " cannot depart : Soi Empty")    
    elif str(n) not in i:
        print("car " + str(n) + " cannot depart : Dont Have Car " + str(n))
    elif str(n) in i:
        print("car "+str(n)+" depart ! : Car "+str(n)+" was remove")
        j = []
        for i in S.items:
            if str(i)!=str(n):
                j.append(i)
        S.items = j
    
print(str(S.items).replace("\'",''))
 