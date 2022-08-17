# จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้

# 1. หาความยาวของ String

# 2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)

# 3. Reverse String (ห้ามใช้คำสั่ง reversed)

# 4. ลบตัวอักษรที่ปรากฏมาก่อนใน String



# class funString():

#     def __init__(self,string = ""):

#         ## Enter Your Code Here ###

#     def __str__(self):

#         ## Enter Your Code Here ###

#     def size(self) :

#         ## Enter Your Code Here ###

#     def changeSize(self):

#         ## Enter Your Code Here ###

#     def reverse(self):

#         ## Enter Your Code Here ###

#     def deleteSame(self):

#        ## Enter Your Code Here ###



# str1,str2 = input("Enter String and Number of Function : ").split()

# res = funString(str1)

# if str2 == "1" :    print(res.size())

# elif str2 == "2":  print(res.changeSize())

# elif str2 == "3" : print(res.reverse())

# elif str2 == "4" : print(res.deleteSame())

class funString():
    def __init__(self, string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def sizeString(self):
        return len(self.string)

    def changesizeString(self):
        temp = ""
        for char in self.string:
            if char.isupper():
                temp += chr(ord(char)-65+97)
            elif char.islower():
                temp += chr(ord(char)+65-97)
        self.string = temp
        return self.string

    def reverseString(self):
        self.string = self.string[::-1]
        return self.string

    def deletesameString(self):
        self.string = "".join(sorted(set(self.string)))
        return self.string
    
str1, str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)

if str2 == "1":
    print(res.sizeString())
elif str2 == "2":
    print(res.changesizeString())
elif str2 == "3":
    print(res.reverseString())
elif str2 == "4":
    print(res.deletesameString())