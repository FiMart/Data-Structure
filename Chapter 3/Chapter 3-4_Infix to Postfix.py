# จงเขียนโปรแกรมเปลี่ยน จาก  Infix expression เป็น Postfix expression ตามตัวอย่าง

# class Stack :

# def __init__(self,list = None) :

# def isEmpty(self) :

# def push(self,data) :

# def pop(self) :

# def size(self) :

# def peek(self) :


# def infix2postfix(exp) :

# s = Stack()

### Enter Your Code Here ###


# print(" ***Infix to Postfix***")

# token = input("Enter Infix expression : ")

# print("PostFix : ")

# print(infix2postfix(token))

class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list()
            
    def isEmpty(self):
        return self.items == []
    
    def push(self, data):
        self.items.append(data)
        
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
def infix2postfix(exp) :
    s = Stack()
    postfix = ""
    
    for items in exp:
        if items.isalpha() == True:
            postfix += items
        elif items == "(":
            s.push(items)
        elif items == ")":          
            while s.peek() != "(":
                postfix += s.pop() 
            s.pop()
        elif items in ("+-*/"):
            if s.isEmpty():
                s.push(items)
            else:
                if (items in ("*","/") and s.peek() in ("+","-") )or s.peek() == "(":
                    s.push(items)
                else:
                    if items in ("+-"):
                        while s.peek() != "(" :
                            postfix += s.pop()
                            if s.isEmpty():
                                break
                    else:
                        while s.peek() not in ("(+-") :
                            postfix += s.pop()
                            if s.isEmpty():
                                break
                    s.push(items)
        elif items == "^" :
            if s.isEmpty():
                s.push(items)
            elif s.peek() != "^":
                s.push(items)
            else:
                 while s.peek() != "^" :
                            postfix += s.pop()
                            if s.isEmpty():
                                break
                            
    while not s.isEmpty():
        postfix += s.pop()
    return postfix

print(" ***Infix to Postfix***")
token = input("Enter Infix expression : ")
print("PostFix : ")
print(infix2postfix(token))
