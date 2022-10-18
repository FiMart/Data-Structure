# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

# จากนั้นหาความสูงของ Binary Search Tree  นั้น

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.data)
    
class binarySearchTree:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            inTree = 0
            temp = self.root
            while(not inTree):
                if temp.data <= data:
                    if temp.right == None:
                        temp.right = Node(data)
                        break
                    else:
                            temp = temp.right
                elif temp.data > data:
                    if temp.left == None:
                        temp.left = Node(data)
                        break
                    else:
                        temp = temp.left
        return self.root
    def printTree(self,node,level = 0):
        if node != None:
            self.printTree(node.right,level + 1)
            print('     ' * level, node)
            self.printTree(node.left,level + 1)
    def clv(self,node,level = 0):
        if node != None:
            l.append(level)
            self.clv(node.right,level + 1)
            self.clv(node.left,level + 1)

l = []
BST = binarySearchTree()
inp = [int(i) for i  in input('Enter Input : ').split()]
for i in inp:
    root = BST.insert(i)
BST.clv(root)
print('Height of this tree is : ' + str(max(l)))
    