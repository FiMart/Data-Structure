# เขียน function Straight Selection Sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

# และแสดงขั้นตอนของ Straight Selection Sort ตามตัวอย่าง

# ***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

# *** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

inp = [int(i) for i in input('Enter Input : ').split()]
a = 0
b = 0

for i in range(len(inp)-1,0,-1):
    for j in range(i):
        if inp[j] > a:
            a = inp[j]
            b = j
    if a > inp[i]:
        inp[b] = inp[i]
        inp[i] = a
        print(f"swap {inp[b]} <-> {inp[i]} : {inp}")
    a = 0
print(inp)