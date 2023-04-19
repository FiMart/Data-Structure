# Chapter : 6 - item : 5 - วาดภาพแสนสุข

# เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

# ****ห้ามใช้คำสั่ง for, while, do while*****

# หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

# def staircase(n):
#     #code here

# print(staircase(int(input("Enter Input : "))))

def staircase(n,i):
    if n>0:
        if i>n:
            pass
        else:
            print(str("_"*(n-i))+str("#"*(i)))
            return staircase(n,i+1)
    elif n<0:
        if i>-n:
            pass
        else:
            print(str("_"*(i-1))+str("#"*((-n)-(i-1))))
            return staircase(n,i+1)
    else:
        print("Not Draw!")

staircase(int(input("Enter Input : ")),1)