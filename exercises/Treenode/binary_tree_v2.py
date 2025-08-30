class Node2:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree2:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value):
        if not self.root:
            self.root = Node2(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.data:
            if node.left:
                self._add(value, node.left)
            else:
                node.left = Node2(value)
        else:
            if node.right:
                self._add(value, node.right)
            else:
                node.right = Node2(value)

    def countNodes(self,node:Node2)->int:
        if node:
            if not node.left and node.right:
                return 1
            else:
                return 1 + self.countNodes(node.left) + self.countNodes(node.right)
        else:
            return 0

    def find(self,value,node:Node2)->Node2 | None:
        if not node:
            return None

        if value == node.data:
            return node

        if value < node.data:
            return self.find(value,node.left)
        else:
            return self.find(value,node.right)


    def pre_order(self,node:Node2):
        if not node:
            return None

        print(node.data,end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node: Node2):
        if not node:
            return None

        self.pre_order(node.left)
        print(node.data, end=' ')
        self.pre_order(node.right)

    def post_order(self, node: Node2):
        if not node:
            return None

        self.pre_order(node.left)
        self.pre_order(node.right)
        print(node.data, end=' ')

    def eval(self,node:Node2)->int:
        if not node:
            return 0

        match node.data:
            case "+":
                return self.eval(node.left) + self.eval(node.right)
            case "-":
                return self.eval(node.left) - self.eval(node.right)
            case "*":
                return self.eval(node.left) * self.eval(node.right)
            case _:
                return node.data





def main():
    bin_tree = BinaryTree2()
    bin_tree.add(4)
    bin_tree.add(3)
    bin_tree.add(5)
    print(bin_tree.countNodes(bin_tree.root))
    print(bin_tree.find(5,bin_tree.root))

    bin_tree.pre_order(bin_tree.root)
    print('')
    bin_tree.in_order(bin_tree.root)
    print('')
    bin_tree.post_order(bin_tree.root)

    node5 = Node2(5)
    node1 = Node2(1)
    node_minus = Node2('-')
    node_minus.left = node5
    node_minus.right = node1

    node2 = Node2(2)
    node_mul = Node2('*')
    node_mul.left = node2
    node_mul.right = node_minus

    node2_2 = Node2(2)
    node3 = Node2(3)
    node_mul_2 = Node2('*')
    node_mul_2.left = node2_2
    node_mul_2.right = node3

    node8 = Node2(8)
    node_plus = Node2('+')
    node_plus.left = node8
    node_plus.right = node_mul_2

    root = Node2('+')
    root.left = node_mul
    root.right = node_plus

    bin_tree2 = BinaryTree2()
    bin_tree.root = root

    print('')

    print(bin_tree2.eval(bin_tree.root))


if __name__ == '__main__':
    main()
