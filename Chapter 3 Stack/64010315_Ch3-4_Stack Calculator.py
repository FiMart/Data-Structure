# Chapter : 3 - item : 4 - Stack Calculator

# # ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
# # +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
# # -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# # *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
# # /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# # DUP: Duplicate (not double) ค่าบนสุดของ stack
# # POP: Pop ค่าบนสุดออกจาก stack และ discard.
# # PSH: ทำการ push ตัวเลขลง stack
# # หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
# # *************************************************
# # print("* Stack Calculator *")
# # arg = input("Enter arguments : ")
# # machine = StackCalc()
# # machine.run(arg)
# # print(machine.getValue())

class StackCalc:
    def __init__(self, lis = None):
        if lis is None:
            self.lis = []
        else:
            self.lis = lis
            
    def pop(self):
        return self.lis.pop()
    
    def push(self,i):
        self.lis.append(i)
        
    def size(self):
        return len(self.lis)
    
    def isEmpty(self):
        return len(self.lis) == 0
    
    def run(self, items ):
        self.bool = True
        for i in items:
            if i in '0123456789':
                self.push(i)
            elif i == '+' and self.lis[-2] :
                obj1 = self.pop()
                obj2 = self.pop()
                obj3 = int(obj1) + int(obj2)
                self.push(int(obj3))
            elif i == '-':
                obj1 = self.pop()
                obj2 = self.pop()
                obj3 = int(obj1) - int(obj2)
                self.push(int(obj3))
            elif i == '*':
                obj1 = self.pop()
                obj2 = self.pop()
                obj3 = int(obj1) * int(obj2)
                self.push(int(obj3))
            elif i == '/':
                obj1 = self.pop()
                obj2 = self.pop()
                obj3 = int(obj1) / int(obj2)
                self.push(int(obj3))    
            elif i =="DUP":
                self.push(self.lis[-1])
            elif i =="POP":
                self.pop()
            elif i in "abcdefghijklmnopqrstuvwxyz":
               self.push(i)
               self.bool = False
               break
            else: 
                self.push(i)

    def getValue(self):
        if self.bool == False:
           return f'Invalid instruction: {self.lis[0]}'
        if len(self.lis) > 0:
            return self.lis[-1]
        else: 
            return '0'
        
print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())