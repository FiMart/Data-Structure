# Chapter : 7 - item : 3 - สีแดงแรง 3 เท่า

# ให้น้องๆรับ input เป็น list และ k โดยให้สร้าง Binary Search Tree จาก list ที่รับมา และหลังจากนั้นให้ทำการดูว่าใน Tree มีค่าไหนที่มากกว่าค่า k หรือไม่ ถ้ามีให้ทำการคูณ 3 เพิ่มเข้าไป

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None
    
    def __str__(self) -> str:
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        a = Node(data)
        if self.root is None:
            self.root = a
            return self.root
        else:
            t=self.root
            while True:
                if data <= t.data:
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

    def printTree(self,node,level=0):
        if node != None:
            self.printTree(node.right,level+1)
            print("     " * level,node)
            self.printTree(node.left,level+1)

    def printDoubleThree(self,node,k,level=0):
        if node != None:
            if node.data > k:
                node.data *= 3
            self.printDoubleThree(node.right,k,level+1)
            print("     " * level,node)
            self.printDoubleThree(node.left,k,level+1)

T = BST()
inp = [int(i) for i in input("Enter Input : ").replace(" ","/").split('/')]
for i in inp[0:-1]:
    T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
T.printDoubleThree(T.root,inp[-1])
