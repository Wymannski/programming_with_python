from re import search


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def count_nodes(self) -> int:
        if self.left and self.right:
            return 1 + self.left.count_nodes() + self.right.count_nodes()
        elif self.left:
            return 1 + self.left.count_nodes()
        elif self.right:
            return 1 + self.right.count_nodes()
        else:
            return 1
    def eval(self):
        if not self.data:
            return 0

        match self.data:
            case '+':
                return self.left.eval() + self.right.eval()
            case '-':
                return self.left.eval() - self.right.eval()
            case '*':
                return self.left.eval() * self.right.eval()
            case '/':
                return self.left.eval() / self.right.eval()
            case _:
                return self.data

class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.data:
            if node.left:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def count_nodes(self)->int:
        if not self.root:
            return 0
        return self.root.count_nodes()

    def count_nodes2(self,node:Node):
        if node:
            if node.left and node.right:
                return 1 + self.count_nodes2(node.left) + self.count_nodes2(node.right)
            else:
                return 1
        else:
            return

    def find(self,root,value):
        if not root or root.data == value:
            return root

        if root.data > value:
            return self.find(root.left,value)

        return self.find(root.right,value)

    def pre_order(self,root):
        if not root:
            return None

        print(root.data,end=' ')
        self.pre_order(root.left)

        self.pre_order(root.right)

    def post_order(self, root):
        if not root:
            return None

        self.post_order(root.left)
        self.post_order(root.right)

        print(root.data, end=' ')

    def in_order(self, root):
        if not root:
            return None

        self.in_order(root.left)

        print(root.data, end=' ')

        self.in_order(root.right)


def main():
    tree = BinaryTree()
    tree.add(50)
    tree.add(20)
    tree.add(55)
    tree.add(11)
    tree.add(46)
    tree.add(15)
    print(tree.count_nodes())
    print(tree.count_nodes2(tree.root))
    print("Found" if tree.find(tree.root,15) else "Not Found")
    print("Found" if tree.find(tree.root,14) else "Not Found")

    tree.pre_order(tree.root)
    print('')
    tree.post_order(tree.root)
    print('')
    tree.in_order(tree.root)


    node5 = Node(5)
    node1 = Node(1)
    node_minus = Node('-')
    node_minus.left = node5
    node_minus.right = node1

    node2 = Node(2)
    node_mul = Node('*')
    node_mul.left = node2
    node_mul.right = node_minus

    node2_2 = Node(2)
    node3 = Node(3)
    node_mul_2 = Node('*')
    node_mul_2.left = node2_2
    node_mul_2.right = node3

    node8 = Node(8)
    node_plus = Node('+')
    node_plus.left = node8
    node_plus.right = node_mul_2

    root = Node('+')
    root.left = node_mul
    root.right = node_plus

    print('')

    print(root.eval())



if __name__ == '__main__':
    main()
