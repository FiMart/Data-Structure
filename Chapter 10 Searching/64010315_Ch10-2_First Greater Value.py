# # Chapter : 10 - item : 2 - First Greater Value

# ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

# ***** อธิบาย Test Case 2:
# Left: [3, 2, 7, 6, 8]         Right: [5, 6, 12]
# 1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list(Left) จะได้เป็น 6
# 2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list(Left) จะได้เป็น 7
# 3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list(Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value

def fgvSearch(l:list,key:int,maxk:int=10e6) -> str:
    if key >= maxk:
        return "No First Greater Value"
    if key in l:
        return str(key)
    return fgvSearch(l,key+1,maxk)

def main():
    inp = input("Enter Input : ").split('/')
    l,key = list(map(int,inp[0].split())), \
        list(map(int,inp[1].split()))
    for i in key:
        print(fgvSearch(l,i+1,max(l)))
        
if __name__ == '__main__':
    main()
