class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cursor, s = self.head, str(self.head.value) + " "
        while cursor.next != None:
            s += str(cursor.next.value) + " "
            cursor = cursor.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cursor, s = self.tail, str(self.tail.value) + " "
        while cursor.previous != None:
            s += str(cursor.previous.value) + " "
            cursor = cursor.previous
        return s

    def isEmpty(self):
        return self.size == 0

    def append(self, items):
        if self.isEmpty():
            self.head = self.tail = Node(items)
            self.size += 1
            return

        newTail = Node(items)
        oldTail = self.tail

        oldTail.next = newTail
        newTail.previous = oldTail
        
        self.tail = newTail
        self.size += 1

    def addHead(self, items):
        if self.isEmpty():
            self.head = self.tail = Node(items)
            self.size += 1
            return
        
        newHead = Node(items)
        oldHead = self.head

        newHead.next = oldHead
        oldHead.previous = newHead

        self.head = newHead
        self.size += 1

    def insert(self, position, items):
        insertNode = Node(items)
        if position == 0:
            self.addHead(items)
            return
        if position > 0:
            if position >= self.size - 1:
                self.append(items)
                return
            else:
                node = self.head
                for i in range(0, position):
                    node = node.next

                previousNode = node
                nextNode = previousNode.next

                previousNode.next = insertNode
                insertNode.previous = previousNode

                nextNode.previous = insertNode
                insertNode.next = nextNode
        else:
            if position <= -self.size:
                self.addHead(items)
                return
            else:
                node = self.tail
                for i in range(-1, position-1, -1):
                    node = node.previous

                previousNode = node
                nextNode = previousNode.next

                previousNode.next = insertNode
                insertNode.previous = previousNode

                nextNode.previous = insertNode
                insertNode.next = nextNode

        self.size += 1

    def search(self, items):
        node = self.head
        while node is not None:
            if node.value == items:
                return "Found"
            node = node.next
        return "Not Found"

    def index(self, items):
        index = 0
        node = self.head
        while node is not None:
            if node.value == items:
                return index
            node = node.next
            index += 1
        return -1

    def size(self):
        return self.size

    def pop(self, position):
        if self.size-1 < position or position < 0:
            return "Out of Range"

        if self.size == 1:
            self.head = None
            self.tail = None

        elif position == 0:
            print(f"l {self}")
            print("size "+ str(self.size))
            newHead = self.head.next
            newHead.previous = None

            self.head = newHead
            
        elif position == self.size-1:
            newTail = self.tail.previous
            newTail.next = None

            self.tail = newTail

        else:
            node = self.head
            for i in range(0, position):
                node = node.next

            previousNode = node.previous
            nextNode = node.next

            if previousNode is not None:
                previousNode.next = nextNode
                nextNode.previous = previousNode

        self.size -= 1
        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size, L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())