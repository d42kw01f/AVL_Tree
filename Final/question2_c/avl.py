import sys


# Create a tree node
class CreateTree(object):
    def __init__(self, data):
        self.root = data
        self.left_stree = None
        self.right_stree = None


class AVLTree(CreateTree):
    def __init__(self, data=None):
        super().__init__(data)
        self.height = 1

    def insert_child(self, node, value):
        if not node:
            return AVLTree(value)
        elif value < node.root:
            node.left_stree = self.insert_child(node.left_stree, value)
        else:
            node.right_stree = self.insert_child(node.right_stree, value)

        node.height = 1 + max(self.update_height(node.left_stree),
                              self.update_height(node.right_stree))

        balanceFactor = self.update_balance(node)
        if balanceFactor > 1:
            if value < node.left_stree.root:
                return self.r_rotate(node)
            else:
                node.left_stree = self.l_rotate(node.left_stree)
                return self.r_rotate(node)

        if balanceFactor < -1:
            if value > node.right_stree.root:
                return self.l_rotate(node)
            else:
                node.right_stree = self.r_rotate(node.right_stree)
                return self.l_rotate(node)

        return node

    def delete_node(self, node, value):
        if not node:
            return node
        elif value < node.root:
            node.left_stree = self.delete_node(node.left_stree, value)
        elif value > node.root:
            node.right_stree = self.delete_node(node.right_stree, value)
        else:
            if node.left_stree is None:
                temp = node.right_stree
                return temp
            elif node.right_stree is None:
                temp = node.left_stree
                return temp
            temp = self.getMinValueNode(node.right_stree)
            node.root = temp.root
            node.right_stree = self.delete_node(node.right_stree,
                                                temp.root)
        if node is None:
            return node

        node.height = 1 + max(self.update_height(node.left_stree),
                              self.update_height(node.right_stree))

        balance_factor = self.update_balance(node)

        if balance_factor > 1:
            if self.update_balance(node.left_stree) >= 0:
                return self.r_rotate(node)
            else:
                node.left_stree = self.l_rotate(node.left_stree)
                return self.r_rotate(node)
        if balance_factor < -1:
            if self.update_balance(node.right_stree) <= 0:
                return self.l_rotate(node)
            else:
                node.right_stree = self.r_rotate(node.right_stree)
                return self.l_rotate(node)
        return node

    def l_rotate(self, z):
        y = z.right_stree
        T2 = y.left_stree
        y.left_stree = z
        z.right_stree = T2
        z.height = 1 + max(self.update_height(z.left_stree),
                           self.update_height(z.right_stree))
        y.height = 1 + max(self.update_height(y.left_stree),
                           self.update_height(y.right_stree))
        return y

    def r_rotate(self, z):
        y = z.left_stree
        T3 = y.right_stree
        y.right_stree = z
        z.left_stree = T3
        z.height = 1 + max(self.update_height(z.left_stree),
                           self.update_height(z.right_stree))
        y.height = 1 + max(self.update_height(y.left_stree),
                           self.update_height(y.right_stree))
        return y

    def update_height(self, curr_node):
        if not curr_node:
            return 0
        return curr_node.height

    def update_balance(self, curr_node):
        if not curr_node:
            return 0
        return self.update_height(curr_node.left_stree) - self.update_height(curr_node.right_stree)

    def getMinValueNode(self, curr_node):
        if curr_node is None or curr_node.left_stree is None:
            return curr_node
        return self.getMinValueNode(curr_node.left_stree)

    def in_order_traversal(self):
        tree_nodes = []

        if self.left_stree:
            tree_nodes += self.left_stree.in_order_traversal()

        tree_nodes.append(self.root)

        if self.right_stree:
            tree_nodes += self.right_stree.in_order_traversal()

        return tree_nodes

    def post_order_traversal(self):
        tree_nodes = []

        if self.left_stree:
            tree_nodes += self.left_stree.post_order_traversal()
        if self.right_stree:
            tree_nodes += self.right_stree.post_order_traversal()
        tree_nodes.append(self.root)

        return tree_nodes

    def pre_order_traversal(self):
        tree_node = [self.root]

        if self.left_stree:
            tree_node += self.left_stree.pre_order_traversal()
        if self.right_stree:
            tree_node += self.right_stree.pre_order_traversal()

        return tree_node

    def printHelper(self, currPtr, indent, last):
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.root)
            self.printHelper(currPtr.left_stree, indent, False)
            self.printHelper(currPtr.right_stree, indent, True)