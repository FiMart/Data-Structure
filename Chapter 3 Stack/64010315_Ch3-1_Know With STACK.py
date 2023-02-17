# Chapter : 3 - item : 1 - รู้จักกับ STACK

# # ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา



# # A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

# # P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

# # *** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

class Stack:
    def __init__(self,list = None):
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
       return self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0

    def Value(self):
        return self.items


inp = input("Enter Input : ").split(',')
S = Stack()
for i in inp:
    L = i.split()
    if L[0] == 'A':
        S.push(L[1])
        print("Add = " + str(L[1]) + " and Size = "+ str(S.size()))
    elif L[0] == 'P':
        if S.size() > 0:
            P = S.pop()
            print("Pop = " + str(P) + " and Index = "+ str(S.size()))
        else:
            print("-1")

print("Value in Stack = ", end="")
if S.size() == 0:
    print("Empty")
else:
    for k in S.Value():
        print(k, end=" ")