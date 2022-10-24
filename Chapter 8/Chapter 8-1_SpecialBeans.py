# กฤษฎาได้ค้นพบเม็ดถั่ววิเศษที่เมื่อโยนลงดินแล้วถั่วจะสามารถเติบโตขึ้นและกลายเป็น Binary Search Tree (BST) ได้ โดยงานของนักศึกษาก็คือนักศึกษาจะต้องสร้าง BST ตามลำดับของข้อมูลนำเข้าซึ่งเป็นตัวเลขจำนวนเต็มที่ไม่ซ้ำกันเลย โดยในการใส่ค่าในแต่ละครั้งจะกลับมาที่ Root of BST เสมอ  แล้วท่องต้นไม้ไปทางซ้ายด้วยคำสั่ง "L" หรือท่องต้นไม้ไปทางขวาด้วยคำสั่ง "R" จนกว่าจะถึงตำแหน่งที่เหมาะสมที่จะใส่ข้อมูลแล้วจึงพิมพ์ "*" เพื่อใส่ข้อมูลลงไปในต้นไม้  จงเขียนโปรแกรมเพื่อแสดงคำสั่งการท่องต้นไม้ในการใส่ข้อมูลทีละค่าตามลำดับของข้อมูลนำเข้า

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
            print('*')
        else:
            inTree = 0
            item = self.root
            while(not inTree):
                if item.data <= data:
                    if item.right == None:
                        item.right = Node(data)
                        print('R*')
                        break
                    else:
                        print('R',end='')
                        item = item.right
                elif item.data > data:
                    if item.left == None:
                        item.left = Node(data)
                        print('L*')
                        break
                    else:
                        print('L',end='')
                        item = item.left
        return self.root
    def printTree(self,node,level = 0):
        if node != None:
            self.printTree(node.right,level+1)
            print('     ' * level, node)
            self.printTree(node.left,level+1)
BST = binarySearchTree()
inp = [int(x) for x in input('Enter Input : ').split()]
for x in inp:
    root = BST.insert(x)