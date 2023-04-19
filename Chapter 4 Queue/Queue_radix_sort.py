class Queue:
    def __init__(self, q = None):
        if q == None:
            self.item = []
        else:
            self.item = q
    def enQ(self, i):
        self.item.append(i)
    def deQ(self):
        return self.item.pop(0)
    def isEmpty(self):
        return self.item == []
    def size(self):
        return len(self.item)

def get_digit(n, d):  #หาค่าหลัก d จาก n  
  for i in range(d-1):
    n //= 10
  return n % 10

def get_max_digit(n):  #หาค่าจำนวนหลักที่มากที่สุด
  i = 0
  while n > 0:
    n //= 10
    i += 1
  return i

def radix_sort(l) :
    q = Queue(l)  #สร้างคิว
    max_bits = get_max_digit(max(l)) #หาค่าจำนวนหลักมากที่สุด
    qq = [Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue(),Queue()]
    #สร้าง list ของคิวเพื่อเก็บตามค่าหลักของตัวเลข เริ่มจาก qq[0],qq[1],...qq[9]
    for i in range (1,max_bits+1) : 
        while not q.isEmpty() :
            num = q.deQ()
            num_digit = get_digit(num,i)
            qq[num_digit].enQ(num)
            #เก็บค่าเลขตั้งต้นตามค่าจำนวนหลักที่ตรวจสอบ
        for i in range (10) :
            while not qq[i].isEmpty() :
                q.enQ(qq[i].deQ())
                #สร้างคิวใหม่ตามการเรียงของค่าของเลขในแต่ละหลัก
    return q.item

rl = radix_sort([45,435,23,1,23,34,99,10,221,2324,555,9,1])
print(rl)




            
