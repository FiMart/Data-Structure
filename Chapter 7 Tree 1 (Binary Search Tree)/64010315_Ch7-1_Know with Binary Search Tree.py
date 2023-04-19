# Chapter: 7 - item: 1 - รู้จักกับ Binary Search Tree

# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def __str__(self):
#         return str(self.data)


# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         # Code Here

#     def printTree(self, node, level=0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)


# T = BST()
# inp = [int(i) for i in input('Enter Input : ').split()]
# for i in inp:
#     root = T.insert(i)
# T.printTree(root)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self) -> None:
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

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)