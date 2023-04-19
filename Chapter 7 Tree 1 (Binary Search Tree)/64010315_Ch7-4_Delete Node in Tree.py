# Chapter : 7 - item : 4 - delete node in tree

# ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

# โดยมีการป้อน input ดังนี้

# i <int> = insert data

# d <int> = delete data

# หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.level = None

#     def __str__(self):
#         return str(self.data)

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, val):
#         #code here
#     def delete(self,r, data):
#         #code here

# def printTree90(node, level = 0):
#     if node != None:
#         printTree90(node.right, level + 1)
#         print('     ' * level, node)
#         printTree90(node.left, level + 1)


# tree = BinarySearchTree()
# data = input("Enter Input : ").split(",")
# #code here

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return self.root
        node = self.root
        while True:
            if val < node.data:
                if node.left == None:
                    node.left = Node(val)
                    return self.root
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(val)
                    return self.root
                node = node.right

    def delete(self, r, data):
        # code here


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
val = input("Enter Input : ").split(",")
# code here
