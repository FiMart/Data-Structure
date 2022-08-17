# อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ



#     โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร
    
print("*** Fun with countdown ***")
print("Enter List : ", end="")

a =  list(map(int, input().split(" ")))
b = -1
c = []
d = []

for e in a:
    if b == -1:
        b = e
        c.append(e)
        if b == 1:
            d.append(c)
            c = []
            b = -1
    elif e == 1:
        c.append(e)
        d.append(c)
        c = []
        b = -1
    elif b - 1 == e:
        c.append(e)
        b = e
    else:
        c = []
        c.append(e)
        b = e

f = []
f.append(len(d))
f.append(d)
print(f)
    
