# นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
# สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน

# ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

# 1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด

# 2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด

# 3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

# ****ห้ามใช้คำสั่ง for, while, do while*****

# หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

def asteroid_collision(asts, x):
    if x >= len(asts) - 1:
        ans = []
        ans = asts
        print(str(ans).replace(" 0,",'').replace("[0, ",'[').replace(", 0]",']').replace('[0]','[]'))
        return 0
    
    if asts[x] < 0:
        if asts[x - 1] >= 0 and x > 0:
            if abs(asts[x]) == asts[x - 1]:
                asts[x - 1] = 0
                asts[x] = 0
                asteroid_collision(asts, x - 1)
            elif max(abs(asts[x]),asts[x - 1]) == abs(asts[x]):
                asts[x - 1] = asts[x]
                asts[x] = 0
                asteroid_collision(asts, x - 1)
            else:
                asts[x] = asts[x - 1]
                asts[x - 1] = 0
                asteroid_collision(asts, x - 1)
        else:
            asteroid_collision(asts, x + 1)
            
    elif asts[x] > 0 and x <= len(asts) - 1:
        if asts[x + 1] <= 0:
            if abs(asts[x + 1]) == asts[x]:
                asts[x + 1] = 0
                asts[x] = 0
                asteroid_collision(asts, x + 1)
            elif max(abs(asts[x + 1]),asts[x]) == asts[x]:
                asts[x + 1] = asts[x]
                asts[x] = 0
                asteroid_collision(asts, x + 1)
            else:
                asts[x] = asts[x + 1]
                asts[x + 1] = 0
                asteroid_collision(asts, x)
        else:
            asteroid_collision(asts, x + 1)
            
    elif asts[x] == 0:
        if x < len(asts) - 1:
            asteroid_collision(asts, x + 1)
        elif x >= len(asts):
            return 0
    
x = input("Enter Input : ").replace(', ',',').split(",")
x = list(map(int, x))
asteroid_collision(x, 0)