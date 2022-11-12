# เขียน function insertion sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

# และแสดงขั้นตอนของ insertion sort ตามตัวอย่าง

# ***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

# *** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

def findIndex(l:list,i:int,end:int) -> int:
    if i < 0 or l[i] < end:
        return i
    l[i+1] = l[i]
    return findIndex(l, i-1, end)

def insertionsortRecursive(l:list,n:int):
    if n <= 1:
        return
    insertionsortRecursive(l, n-1) 
    end = l[n-1]   
    i = findIndex(l, n-2, end)
    l[i+1] = end 
    print(f'insert {end} at index {i+1} : ',end='')
    print(f'{l}' if len(l) == n else f'{l[:n]} {l[n:]}')

def main():
    inp = list(map(int, input("Enter Input : ").split()))
    insertionsortRecursive(inp,len(inp)) or print(f'sorted\n{inp}')

if __name__ == '__main__':
    main()

    