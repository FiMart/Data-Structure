# ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function

# ถ้าหากเป็น 1 argument -> range(a)            | start = 0 , end = a , step = 1

# ถ้าหากเป็น 2 argument -> range(a, b)        | start = a , end = b , step = 1

# ถ้าหากเป็น 3 argument -> range(a, b, c)    | start = a , end = b , step = c

def newRange(number): 
    x = []
    if len(number) == 1:
        y=0.0
        while y<number[0]:
            x.append(y)
            y+=1
    elif len(number)==2:
        y=number[0]
        while y<number[1]:
            x.append(y)
            y+=1
    else:
        y=number[0]
        while y<number[1]:
            x.append(y)
            y+=number[2]
    return x

print("*** New Range ***")
number=[float(i) for i in input("Enter Input : ").split()]
z=newRange(number)
for i in range(len(z)):
    z[i]=float("{:.3f}".format(z[i]))
print(tuple(z))