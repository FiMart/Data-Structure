# Chapter : 7 - item : 5 - Expression Tree

# ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

class Node:
    def __init__(self, data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else :
            inTree = 0
            cur = self.root
            while(not inTree):
                if cur.data <= data:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    else :
                        cur = cur.right
                elif cur.data > data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else :
                        cur = cur.left
        return self.root 
           
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
def postToPre(postExp):
    l = []
    for i in range(len(postExp)):
        if (postExp[i]in "+-*/"):
            Op1 = l[-1]
            l.pop()
            Op2 = l[-1]
            l.pop()
            temp = postExp[i] + Op2 + Op1
            l.append(temp)
        else:
            l.append(postExp[i]) 
    ans = ""
    for i in l:
        ans += i
    return ans

def postToIn(postExp):
    l = []
    for i in range(len(postExp)):
        if (postExp[i]in"+-*/"):
            Op1 = l[-1]
            l.pop()
            Op2 = l[-1]
            l.pop()
            temp = '(' + Op2 + postExp[i] + Op1 + ')'
            l.append(temp)
        else:
            l.append(postExp[i])    
    ans = ""
    for i in l:
        ans += i
    return ans

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
        
BST = BST()
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