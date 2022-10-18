# ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)
    
class binarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else :
            inTree = 0
            temp = self.root
            while(not inTree):
                if temp.data <= data:
                    if temp.right == None:
                        temp.right = Node(data)
                        break
                    else :
                        temp = temp.right
                elif temp.data > data:
                    if temp.left == None:
                        temp.left = Node(data)
                        break
                    else :
                        temp = temp.left
        return self.root 
           
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
def postToPre(postExp):
    s = []
    for i in range(len(postExp)):
        if (postExp[i]in "+-*/"):
            Op1 = s[-1]
            s.pop()
            Op2 = s[-1]
            s.pop()
            temp = postExp[i] + Op2 + Op1
            s.append(temp)
        else:
            s.append(postExp[i]) 
    answer = ""
    for i in s:
        answer += i
    return answer

def postToIn(postExp):
    s = []
    for i in range(len(postExp)):
        if (postExp[i]in"+-*/"):
            Op1 = s[-1]
            s.pop()
            Op2 = s[-1]
            s.pop()
            temp = '(' + Op2 + postExp[i] + Op1 + ')'
            s.append(temp)
        else:
            s.append(postExp[i])    
    answer = ""
    for i in s:
        answer += i
    return answer

class stack():
    def __init__(self):
        self.s = []
        
    def push(self,data):
        self.s.append(data)
        
    def isEmpty(self):
        return len(self.s)==0
    
    def peek(self):
        if not self.isEmpty():
            return self.s[-1]
        
    def pop(self):
        if not self.isEmpty():
            return self.s.pop()
        
BST = binarySearchTree()
ST = stack()
inp = input('Enter Postfix : ')
for i in inp:
    if i in '+-*/':
        r = ST.pop()
        l = ST.pop()
        ST.push(Node(i,l,r))
    else :
        ST.push(Node(i))
print("Tree :")
BST.root = ST.pop()
BST.printTree(BST.root)
print('--------------------------------------------------')
print("Infix :", postToIn(inp))
print("Prefix :",postToPre(inp))