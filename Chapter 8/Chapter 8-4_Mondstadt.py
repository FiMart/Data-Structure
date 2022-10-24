# Jean รักษาการผู้บัญชาการของกองอัศวิน Favonius แห่ง Mondstadt ต้องการทราบถึงขุมพลังของอัศวินในแต่ละกลุ่มภายในเมือง Mondstadt แห่งนี้จึงจะทดสอบความแข็งแกร่งของขุมกำลังที่มี โดยจะทำการจัดวางกำลังอัศวินภายในเมือง Mondstadt ดังตัวอย่างต่อไปนี้
#                 พลัง    :   5  4  4  3  2  2  2
#                 ลำดับ  :   0  1  2  3  4  5  6
# จากข้อมูลข้างต้นประกอบด้วยอัศวินทั้งหมด 7 คน เรียงตามลำดับตั้งแต่ลำดับที่ 0 ถึง 6 และพลังของอัศวินแต่ละคนมีข้อกำหนดดังนี้
#     -  อัศวินลำดับที่ n จะมีลูกน้องในสังกัดอยู่ลำดับที่ 2n+1 และ 2n+2 (ลูกน้องของลูกน้องของอัศวินลำดับที่ n ถือว่าเป็นลูกน้องของอัศวินลำดับที่ n ด้วย)
#     -  ค่าพลังของอัศวินมีค่าตั้งแต่ 0 - 5
#     -  กลุ่มของอัศวินกลุ่มที่ i จะมีสมาชิกคือ อัศวินลำดับที่ i และลูกน้องของอัศวินลำดับที่ i (รวมลูกน้องของลูกน้องของอัศวินด้วย)
#     -  พลังของกลุ่มอัศวินลำดับที่ i เป็นพลังรวมของสมาชิกของอัศวินทั้งหมดในกลุ่ม เช่น
#             -  อัศวินกลุ่มที่ 1 หมายถึง กลุ่มของอัศวินลำดับที่ 1 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 1, 3 และ 4 และค่าพลังรวมของอัศวินกลุ่มที่ 1 เท่ากับ 4 + 3 + 2 = 9
#             -  อัศวินกลุ่มที่ 2 หมายถึง กลุ่มของอัศวินลำดับที่ 2 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 2 , 5 และ 6 และค่าพลังรวมของอัศวินกลุ่มที่ 2 เท่ากับ 4 + 2 + 2 = 8

# ดังนั้นเมื่อนำพลังของอัศวินกลุ่มที่ 1 และ 2 มาเทียบกัน จะได้ว่าพลังรวมของอัศวินกลุ่มที่ 1 นั้นมากกว่าพลังรวมของอัศวินกลุ่มที่ 2
# Jean ต้องการทราบว่าค่าพลังรวมของอัศวินภายในเมือง Mondstadt เป็นเท่าใด และถ้าเปรียบเทียบระหว่างอัศวินแต่ละกลุ่มแล้วค่าของพลังรวมของอัศวินในกลุ่มใดมีค่ามากกว่ากัน

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        
    def __str__(self) -> str:
        return str(self.data)
    
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
        if z is not None:
            z.height = max(self.getHeight(z.left),self.getHeight(z.right))+1
            return z.height
        else:
            return -1
        
    def insert(self,node,data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        else:
            if node is not None:
                if data <= node.data:
                    node.left = self.insert(node.left,data)
                else:
                    node.right = self.insert(node.right,data)
            else:
                return Node(data)
            
            Left = node.left.height if node.left != None else -1
            Right = node.right.height if node.right != None else -1
            if abs(Left - Right) > 1:
                z = self.root
                if Left > Right:
                    if data <= node.left.data:
                        z = self.LeftLeft(node)
                    else:
                        node.left = self.RightRight(node.left)
                        node = self.LeftLeft(node)
                        z = node
                else:
                    if data <= node.right.data:
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
            
def printTree(node,level = 0):
    if node is not None:
        printTree(node.right,level + 1)
        print('     ' * level, node)
        printTree(node.left,level + 1)
        
def dataFill(node,data,d=[]):
    if node is not None:
        if node.left is not None:
            d.append(node.left)
        if node.right is not None:
            d.append(node.right)
        node.data = data.pop(0)
        if len(d) is not 0:
            dataFill(d.pop(0),data,d)

def getPower(node):
    if node is not None:
        return node.data + getPower(node.left) + getPower(node.right)
    return 0

def findNode(node,a,i=0,d=[]):
    if node is not None:
        if node.left is not None:
            d.append(node.left)
        if node.right is not None:
            d.append(node.right)
        if i == a:
            return node
        return findNode(d.pop(0),a,i+1,d)
    
def comPare(root,i,j):
    cI = getPower(findNode(root,i,0,[]))
    cJ = getPower(findNode(root,j,0,[]))
    if cI < cJ:
        print(str(i) + "<" + str(j))
    elif cI > cJ:
        print(str(i) + ">" + str(j))
    else:
        print(str(i) + "=" + str(j))
        
T = AVL()
root = None
inp,comp = input("Enter Input : ").split('/')
data = [int(i) for i in inp.split()]
for i in data:
    root = T.insert(root,'x')
dataFill(root,data)
print(getPower(root))
for i in comp.split(','):
    comPare(root,int(i.split()[0]),int(i.split()[1]))