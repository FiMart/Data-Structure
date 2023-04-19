# Chapter : 7 - item : 2 - หาค่า height

# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

# จากนั้นหาความสูงของ Binary Search Tree  นั้น

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left is None:
                        cur.left = Node(data)
                        break
                    cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = Node(data)
                        break
                    cur = cur.right
        return self.root
    
    def printTree(self, node, level = 0):
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
BST =BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:
    root = BST.insert(i)
BST.clv(root)
print("Height of this tree is : " + str(max(l)))
            