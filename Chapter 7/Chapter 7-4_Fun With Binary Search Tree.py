# ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return str(self.data)

class Queue:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)

class binarySearchTree:
    def __init__(self) -> None:
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
    
    def preOrder(self,node):
        if node == None:
            return ''

        s = str(node.data) + ' '\
            + self.preOrder(node.left)\
                + self.preOrder(node.right)
        return s

    def inOrder(self,node):
        if node == None:
            return ''

        s = self.inOrder(node.left)\
             + str(node.data) + ' '\
                 + self.inOrder(node.right)
        return s

    def postOrder(self,node):
        if node == None:
            return ''
        
        s = self.postOrder(node.left)\
            + self.postOrder(node.right)\
                + str(node.data) + ' '
        return s

    def BFS(self): 
        q = Queue()
        q.enqueue(self.root)
        s = "Breadth : "
        while not q.isEmpty():
            node = q.dequeue()
            s += str(node.data) + ' '
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return s

BST = binarySearchTree()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = BST.insert(i)
    
print('Preorder :', BST.preOrder(root))
print('Inorder :', BST.inOrder(root))
print('Postorder :', BST.postOrder(root))
print(BST.BFS())
        
        