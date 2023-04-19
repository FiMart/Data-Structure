# Chapter : 3 - item : 2 - Number in Stack

# # จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

# # A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

# # P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

# # D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

# # LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

# # MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

# # การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

# # *** Hint ***

# # ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,data):
        self.items.append(data)
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Empty stack")
            return -1
        
    def pop(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print("Empty stack")
            return -1
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def copy(self,l):
        self.items = l
    
    def value(self):
        return self.items
        
    def castlisttoint(self):
        for i in range(len(self.items)):
            self.items[i] = int(self.items[i])
            
def ManageStack(inp):
    S = Stack()

    def A(n):
        S.push(n)
        print("Add = "+str(n))

    def P():
        if S.size() > 0:
            p = S.pop()
            print("Pop = "+str(p))
        else:
            print("-1")

    def D(n):
        d = Stack()
        if S.size() > 0 :
            for i in S.value():
                if i != n :
                    d.push(i)
                else :
                    print("Delete = "+ str(n))
            S.copy(d.value())
        else:
            print("-1")
    
    def LD(n):
        LD = Stack()
        li = S.value()
        li.reverse()
        if S.size() > 0 :
            for i in li:
                if int(i) >= int(n) :
                    LD.push(i)
                else :
                    print("Delete = " + str(i) + " Because " + str(i) + " is less than " + str(n))
            LDlist = LD.value()
            LDlist.reverse()
            S.copy(LDlist)
        else:
            print("-1")

    def MD(n):
        MD = Stack()
        li = S.value()
        li.reverse()
        if S.size() > 0 :
            for i in li:
                if int(i) <= int(n) :
                    MD.push(i)
                else :
                    print("Delete = " + str(i) + " Because " + str(i) + " is more than " + str(n))
            MDlist = MD.value()
            MDlist.reverse()
            S.copy(MDlist)
        else:
            print("-1")

    for i in inp:
        L = i.split()
        if L[0] == "A":
            A(L[1])
        elif L[0] == "P":
            P()
        elif L[0] == "D":
            D(L[1])
        elif L[0] == "LD":
            LD(L[1])
        elif L[0] == "MD":
            MD(L[1])
    S.castlisttoint()
    print("Value in Stack = " + str(S.value()))
l = input("Enter Input : ").split(',')
ManageStack(l)