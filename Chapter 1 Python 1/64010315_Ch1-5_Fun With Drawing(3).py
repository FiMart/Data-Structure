# Chapter : 1 - item : 5 - สนุกไปกับการวาดรุป(3)

# # เขียนภาษา Python เพื่อวาดรูปหยิน-หยาง ซึ่งจะรับ input เป็นขนาดของรูปหยิน-หยาง

n = int(input('Enter Input : '))
for i in range(n+1):
    print("."*(n-i+1),end="")
    print("#"*(i+1),end="")
    if(i==0):
        print("+"*(n+2),end="")
    else:
        print("+",end="")
        print("#"*n,end="")
        print("+",end="")
    print()
for i in range(2):
    print("#"*(n+2),end="")
    print("+"*(n+2),end="")
    print()
for i in range(n):
    print("#",end="")
    print("+"*n,end="")
    print("#",end="")
    print("+"*(n+1-i),end="")
    print("."*(i+1),end="")
    print()
print("#"*(n+2),end="")
print("+",end="")
print("."*(n+1))

