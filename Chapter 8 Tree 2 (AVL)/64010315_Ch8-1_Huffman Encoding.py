# Chapter : 8 - item : 1 - Huffman Encoding

# ให้นักศึกษาเขียนโปรแกรมในการเข้ารหัส Huffman (บีบอัดข้อมูล) โดยใช้ Tree และแสดงผลตามตัวอย่าง

# #อ่านวิธีการเข้ารหัสได้ที่ http://datastructurealgori.blogspot.com/2017/06/huffmans-code.html

def main():
    inp = list(input("Enter Input : "))
    data = set(inp)

    tree = Tree()
    for e in data:
        node = Node(e, inp.count(e))
        tree.insert(node)

    node_list = tree.inorder(tree.root)
    temp_list = [node_list.pop()]

    while len(node_list) != 0 or len(temp_list) != 1:
        if len(temp_list) > 1:
            if len(node_list) == 0 or \
                (node_list[-1].freq >= temp_list[0].freq + temp_list[1].freq):
                left_node = temp_list.pop(0)
                right_node = temp_list.pop(0)
                temp_list.append(tree.merge_tree(left_node, right_node))
            else:
                temp_list.append(node_list.pop())
        else:
            temp_list.append(node_list.pop())

    huffman = temp_list.pop(0)

    encode_dict = {}
    encode_dict = traverse_and_dict(huffman, encode_dict)
    print(encode_dict)

    tree.print(huffman)

    print("Encoded! : ", end="")
    for d in inp:
        print(encode_dict[d], end="")
    print()

def traverse_and_dict(root, encode_dict, value=""):
    if not root.left and not root.right:
        encode_dict[root.data] = value
        return encode_dict
    dict_right = {}
    if root.right:
        dict_right = traverse_and_dict(root.right, encode_dict, value + "1")
    dict_left = {}
    if root.left:
        dict_left = traverse_and_dict(root.left, encode_dict, value + "0")
    return {**dict_left, **dict_right}

class Node:
    def __init__(self, data=None, freq=0):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def print(self, root, level=0):
        if root:
            self.print(root.right, level + 1)
            print(level * "     ", root)
            self.print(root.left, level + 1)

    def insert(self, node, curr=None):
        if not self.root:
            self.root = node
            return
        if not curr:
            curr = self.root

        if node.freq > curr.freq:
            if curr.right:
                self.insert(node, curr.right)
            else:
                curr.right = node
        elif node.freq == curr.freq:
            if node.data < curr.data:
                if curr.left:
                    self.insert(node, curr.left)
                else:
                    curr.left = node
            else:
                if curr.right:
                    self.insert(node, curr.right)
                else:
                    curr.right = node
        elif node.freq < curr.freq:
            if curr.left:
                self.insert(node, curr.left)
            else:
                curr.left = node

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.right) + \
                [Node(node.data, node.freq)] + \
                self.inorder(node.left)

    def merge_tree(self, left, right):
        freq = left.freq + right.freq
        node = Node("*", freq)
        node.left = left
        node.right = right
        return node


if __name__ == "__main__":
    main()