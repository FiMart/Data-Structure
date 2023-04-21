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
        a = Node(val)
        if self.root is None:
            self.root = a
            return self.root
        else:
            t=self.root
            while True:
                if val <= t.data:
                    if t.left is None:
                        t.left = a
                        return self.root
                    else:
                        t = t.left
                else:
                    if t.right is None:
                        t.right = a
                        return self.root
                    else:
                        t = t.right

    def delete(self, r, data):
        if r is None:
            print("Error! Not Found DATA")
            return
        if r.data != data: 
            if data<r.data:
                r.left = self.delete(r.left, data) 
            elif data> r.data:
                r.right = self.delete(r.right, data)  
        else:   

            if r.left is None:   
                r = r.right
                return r
            elif r.right is None:  
                r = r.left
                return r
            else:
                current = r.right
                while current.left is not None:
                    current = current.left

                r.data = current.data    
                
                r.right = self.delete(r.right, current.data)
        return r

    def printTree90(self,node, level=0):
        if node != None:
            self.printTree90(node.right, level + 1)
            print('     ' * level, node)
            self.printTree90(node.left, level + 1)


tree = BinarySearchTree()
val = input("Enter Input : ").split(",")
for i in range(len(val)):
    if val[i][0] == 'i':
        print("insert " + (val[i][2:]))
        tree.root = tree.insert(int(val[i][2:]))
        tree.printTree90(tree.root)
    if val[i][0] == 'd':
        print("delete " + (val[i][2:]))
        tree.root = tree.delete(tree.root, int(val[i][2:]))
        tree.printTree90(tree.root)
