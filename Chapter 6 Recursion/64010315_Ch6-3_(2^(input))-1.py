# Chapter : 6 - item : 3 - ( 2^(input) ) - 1

# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! !

# *** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11

def permutation(l):
    if l == []:
        print("0")
        return 1
    elif 2 in l:
        i = l.index(2)
        if i == 0:
            return 1
        l[i-1] += 1
        l[i] = 0
        return permutation(l)
    else:
        print("".join([str(i) for i in l]))
        l[-1] += 1
        return permutation(l)

n = int(input("Enter Number : "))
if n < 0:
    print("Only Positive & Zero Number ! ! !")
    exit()
permutation([0]*n)
