# Chapter : 2 - item : 3 - Mod Position

# # ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการแสดงตำแหน่งของ List ในตำแหน่งที่หารเลขใดๆลงตัว จาก String

# # def mod_position(arr, s):
# #     Code Here

# # Input ตำแหน่งที่แรกเป็นค่าใน String ที่นำเข้ามา

# # Input ตำแหน่งที่สองเป็นตัวเลขที่ทำการบอกว่าจะแสดงที่ตำแหน่งที่หารตัวเลขนั้นๆลงตัว เช่นถ้าใส่เลข 3 และ String มีค่าเป็น ABCDEFG ก็จะแสดงตำแหน่งที่ 3 คือ C กับตำแหน่งที่ 6 คือ F 

# def mod_position(arr, s):
#     # Code

def mod_position(arr, s):
    list=[]
    for n in range(0,len(arr)-2):
        if((n+1)%s==0):
         list.append(arr[n])
    return list

print("*** Mod Position ***")   
string= input("Enter Input : ")
number=int(string[-1])
print(mod_position(string,number))