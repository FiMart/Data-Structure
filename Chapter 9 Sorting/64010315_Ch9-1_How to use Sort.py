# Chapter : 9 - item : 1 - หัดใช้ Sort

# ให้น้องๆทำการตรวจสอบว่า input ที่เราใส่ลงไปนั้นได้มีการเรียงลำดับมาแล้วหรือไม่ ถ้าหากเรียงมาแล้วให้แสดงผลเป็น Yes แต่ถ้าหากไม่ให้แสดงผลเป็น No

# ****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

if __name__ == "__main__":
    inp = list(map(int, input("Enter Input : ").split()))
    #inp = list(map(int, "5252 -5 2630 -558".split()))
    for i in range(1, len(inp)):
        #print(inp[i-1], inp[i])
        if inp[i-1] > inp[i]:
            print("No")
            break
    else:
        print("Yes")
