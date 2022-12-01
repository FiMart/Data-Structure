# ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

# 1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
# 2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
# 3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
# 4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)

# อธิบาย Input
# แบ่ง Data เป็น 2 ชุดด้วย /
#     -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
#     -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, tSize, maxColl):
        self.tSize = tSize
        self.maxColl = maxColl
        self.table = [None for i in range(tSize)]

    def full(self) -> None:
        if not None in self.table:
            print("This table is full !!!!!!")
            exit()

    def insert(self, key: str, val: str) -> None:
        self.full()
        coll = 0
        bIdx = idx = sum(ord(i) for i in key)%self.tSize
        while self.table[idx]:
            coll+=1
            print(f"collision number {coll} at {idx}")
            if coll == self.maxColl:
                print("Max of collisionChain")
                break
            idx = (bIdx+(coll**2))%self.tSize
        if not self.table[idx]:
            self.table[idx] = Data(key,val)

    def __str__(self):
        s = str()
        for i,val in enumerate(self.table):
            s += f"#{i+1}	{val}\n"
        return s + "---------------------------"

def main():
    print(" ***** Fun with hashing *****")
    inp = input("Enter Input : ").split('/')
    tSize, maxColl = int(inp[0].split()[0]),int(inp[0].split()[1])
    hash = Hash(tSize,maxColl)
    for i in inp[1].split(','):
        key, val = i.split()
        hash.insert(key,val) or print(hash)

if __name__ == '__main__':
    main()