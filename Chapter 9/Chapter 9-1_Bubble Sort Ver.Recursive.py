# เขียน function bubble sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

# ***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

# *** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

def bubblesortRecursive(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
           if list[j] > list[j+1]:
               list[j],list[j+1] = list[j+1],list[j]

inp = list(map(int,input("Enter Input : ").split()))
bubblesortRecursive(inp)
print(inp) 
    