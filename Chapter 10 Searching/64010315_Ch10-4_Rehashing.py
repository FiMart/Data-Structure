# Chapter: 10 - item: 4 - Rehashing

# ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
# 1. Table เต็มถึงระดับที่กำหนด (Threshold ( % ))
# 2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

# หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

# การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

# อธิบาย Input
# แบ่ง Data เป็น 2 ชุดด้วย /
#     -   ด้านซ้ายหมายถึง ขนาดของ Table, MaxCollision และ Threshold (สูงสุด 100 % ) ตามลำดับ
#     -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด

class Data:
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

class Hash:
    def __init__(self, tSize, maxColl, threShold):
        self.tSize = tSize
        self.maxColl = maxColl
        self.threshold = threShold
        self.duplTable = list()
        self.table = [None for i in range(tSize)]
    
    def rehashTsize(self,n:int) -> int:
        n *= 2
        while True:
            factorial, n = 0, n+1
            for i in range(2, n):
                factorial += 1 if n%i==0 else 0
                if factorial>1:
                    break
            if factorial == 0:
                break
        return n 

    def rehashResize(self) -> None:
        self.tSize = self.rehashTsize(self.tSize)
        self.table = [None for i in range(self.tSize)]
    
    def rehashInsert(self) -> None:
        for i in self.duplTable:
            bIdx = idx = i%self.tSize
            coll = 0
            while self.table[idx]:
                coll+=1
                print(f"collision number {coll} at {idx}")
                if coll == self.maxColl:
                    break
                idx = (bIdx+coll**2)%self.tSize
            if not self.table[idx]:
                self.table[idx] = i

    def insert(self, val: int) -> None:
        print(f"Add : {val}")
        b_idx = idx = val%self.tSize
        coll = 0
        while self.table[idx]:
            coll += 1
            print(f"collision number {coll} at {idx}")
            if coll == self.maxColl:
                print("****** Max collision - Rehash !!! ******")
                self.rehashResize() or self.rehashInsert()
                idx = val%self.tSize
                break
            idx = (b_idx+(coll**2))%self.tSize 
        self.duplTable.append(val)
        if len(self.duplTable)*100/self.tSize >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehashResize() or self.rehashInsert()
        else:
            self.table[idx] = Data(val)

    def __str__(self):
        s = str()
        for i,val in enumerate(self.table):
            s += f"#{i+1}	{val}\n"
        return s + "----------------------------------------"

def main():
    print(" ***** Rehashing *****")
    inp = input("Enter Input : ").split('/')
    tSize, maxColl, threShold = int(inp[0].split()[0]),int(inp[0].split()[1])\
        ,int(inp[0].split()[2])
    hash = Hash(tSize,maxColl,threShold)
    print("Initial Table :")
    print(hash)
    for i in inp[1].split():
        hash.insert(int(i)) or print(hash)

if __name__ == '__main__':
    main()