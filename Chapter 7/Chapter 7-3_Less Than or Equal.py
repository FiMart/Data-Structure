# ให้น้องรับ input เป็น list กับ k และจากนั้นให้สร้าง Binary Search Tree จาก list ที่รับเข้ามา และหาว่าใน Binary Search Tree นั้นมีกี่ Node ที่มีค่าน้อยกว่าหรือเท่ากับ k

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class binarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                    return self.root
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right
    
    def printTree(self,node,level = 0):
        if node != None:
            self.printTree(node.right,level + 1)
            print('     ' * level, node)
            self.printTree(node.left,level + 1)

    def lessThan(self,node,data):
        if node == None:
            return 0

        s = self.lessThan(node.left,data)
        if node.data > data:
            return s
        s += self.lessThan(node.right,data)

        if node.data <= data:
            s += 1
        return s


BST = binarySearchTree()
inp,x = input('Enter Input : ').split('/')
inp = [int(i) for i in inp.split()]
for i in inp:
    root = BST.insert(i)
BST.printTree(root)
print('--------------------------------------------------')
print(BST.lessThan(root, int(x)))
            