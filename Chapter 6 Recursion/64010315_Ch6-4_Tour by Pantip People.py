# Chapter : 6 - item : 4 - ไปเที่ยวแบบชาว Pantip

# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 ) ******

# หลังจากที่กฤษฎาสอบมิดเทอมเสร็จ กำลังเดินทางกลับบ้านก็ได้หยิบโทรศัพท์ขึ้นมาเช็คข่าวสารต่างๆ แต่ก็ต้องสะดุดสิ่งที่เพื่อนของกฤษฎานั้นแชร์มาให้ นั่นคือกระทู้ที่มีหัวข้อว่า "ทริปไปเที่ยวโดยใช้ตังน้อยที่สุด" by Pantip กฤษฎาก็ได้เข้ากระทู้ไปอ่านจึงได้สะดุดกับบางประโยคของกระทู้นี้  นั่นคือการคำนวณว่าถ้าหากเรามีเงิน k บาท เราสามารถซื้อของให้เงินหมดพอดี (ไม่เหลือไม่ขาด) ได้หรือไม่ ถ้าได้จะได้สินค้าราคาเท่าใดบ้าง (หาทุกค่าที่ซื้อได้)  ถึงแม้ว่าของจะมีราคาเท่ากันก็ถือว่าเป็นของคนละชิ้นอยู่ดี  กฤษฎาจึงได้อยากไหว้วานน้องๆปีสอง วิศวกรรมคอมพิวเตอร์ ในการช่วยเขียนโปรแกรมแบบ Recursive ในการช่วยหาว่ากฤษฎาจะซื้อของได้ทั้งหมดกี่แบบและแต่ละแบบมีราคาของเท่าไหร่บ้าง

# ****** รายละเอียด Input ******
# โดย Input จะแบ่งเป้นทั้งหมด 2 ฝั่ง ได้แก่   ซ้าย : จำนวนเงินที่กฤษฎามี   |    ขวา : ราคาของสินค้าแต่ละชิ้น

# ****** Output ******
# รับประกันว่ากฤษฎาจะซื้อของได้อย่างน้อย 1 pattern

# def pantip(k, n, arr, path):
#     # Code Here

# inp = input('Enter Input (Money, Product) : ').split('/')
# arr = [int(i) for i in inp[1].split()]
# pattern = pantip(int(inp[0]), 0, arr, [])
# print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))

def pantip(k, n, arr, path):
    possible = 0
    if arr == []:
        return
    if n+arr[0] > k:
        pan = pantip(k,n,arr[1:],path)
        if pan is not None:
            possible += pan
    elif n+arr[0] < k:
        path.append(arr[0])
        pan = pantip(k,n+arr[0],arr[1:],path)
        if pan is not None:
            possible += pan
        path.pop()
        pan = pantip(k,n,arr[1:],path)
        if pan is not None:
            possible += pan
    elif n+arr[0] == k:
        path.append(arr[0])
        possible += 1
        print(str(path).replace('[','').replace(']','').replace(',',''))
        path.pop()
        pan = pantip(k,n,arr[1:],path)
        if pan is not None:
            possible += pan
        return possible
    return possible

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))