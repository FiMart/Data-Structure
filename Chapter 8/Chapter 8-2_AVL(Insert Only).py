# ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert และปรับ Balance เรียบร้อยแล้ว



# ** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

class Node: 
    def __init__(self, val) -> None: 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self) -> str:
        return str(self.val)
  
class AVL: 
    def __init__(self) -> None:
        self.root = None
    
    def RightRight(self,x):
        y = x.right
        x.right = y.left
        y.left = x
        return y
    
    def LeftLeft(self,x):
        y = x.left
        x.left = y.right
        y.right = x
        return y
    
    def getHeight(self,z):
        if z!=None:
            z.height = max(self.getHeight(z.left),self.getHeight(z.right))+1
            return z.height
        else:
            return -1
    
    def insert(self,node,data):
        data = int(data)
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            if node is not None:
                if data < node.val:
                    node.left = self.insert(node.left,data)
                else:
                    node.right = self.insert(node.right,data)
            else:
                return Node(data)
            
            
            Left = node.left.height if node.left != None else -1
            Right = node.right.height if node.right != None else -1
            
            if abs(Left - Right)>1:
                z = self.root
                if Left > Right:
                    if data < node.left.val:
                        z = self.LeftLeft(node)
                    else:
                        node.left = self.RightRight(node.left)
                        node = self.LeftLeft(node)
                        z = node
                else:
                    if data < node.right.val:
                        node.right = self.LeftLeft(node.right)
                        node = self.RightRight(node)
                        z = node
                    else:
                        z = self.RightRight(node)
                self.getHeight(z)
                return z
            else:
                node.height = max(Left,Right)+1
                return node

def printTree(node, level = 0):
    if node is not None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)
  
myTree = AVL() 
root = None
inp = input("Enter Input : ").split()
for i in inp:
    print('Insert : ( ' + i +' )')
    root = myTree.insert(root, i)
    printTree(root)
    print("--------------------------------------------------")
            
    