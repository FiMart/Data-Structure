# Chapter : 4 - item : 1 - html tag

# # จงแก้ไข class Stack และส่วนของโปรแกรมต่อไปนี้ เพื่อให้ทำงานได้อย่างถูกต้อง โปรแกรมนี้เป็นโปรแกรมสำหรับตรวจสอบ เอกสาร HTML ว่ามีความถูกต้องหรือไม่

# # class Stack :
# #     def __init__(self,list = None) :
# #         if list == None :
# #             self.item = []
# #         else :
# #             self.item = list()

# #     def isEmpty(self) :
  
# #     def push(self,i) :
    
# #     def pop(self) :

# #     def size(self) :


# # def isMatchedHtml(raw):
# #     S = Stack()
# #     j = raw.find('<')
# #     while j != -1:
# #         k = raw.find('>', j+1)
# #         if k == -1:
# #             return False
# #         tag = raw[j+1:k]
# #         if not tag.startswith('/'):
# #             S.push(tag) 
# #         else:
# #             if S.isEmpty(): 
# #                 return False
# #             if tag[1:] != S.pop(): 
# #                 return False
# #         j = raw.find('<' , k+1) 
# #     return S.isEmpty()

# # raw = input("Enter HTML content : ")
# # if isMatchedHtml(raw)):
# #     print ("This is match tag HTML")
# # else:
# #     print("This is not match tag HTML")

class Stack:
    def __init__(self,list = None):
        if list == None:
            self.item = []
        else:
            self.item = list()
    
    def isEmpty(self):
        return self.item == []
    
    def push(self,data):
        self.item.append(data)
        
    def pop(self):
        return self.item.pop()
    
    def size(self):
        return len(self.item)
    
def isMatchedHtml(self):
    S = Stack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>',j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith("/"):
            S.push(tag)
        else:
            if S.isEmpty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<',k+1)
    return S.isEmpty()

raw = input("Enter HTML content : ")
if isMatchedHtml(raw):
    print("This is match tag HMTL")
else:
    print("This is not match tag HTML")