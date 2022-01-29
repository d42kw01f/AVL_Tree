import sys


class CreateTree(object):
    def __init__(self, data):
        self.root = data
        self.left_stree = None
        self.right_stree = None


class AVLTree(CreateTree):
    def __init__(self, data=None):
        super().__init__(data)
        self.height = 1

    def insert_node(self, node, value):
        if not node:
            return AVLTree(value)
        elif value < node.root:
            node.left_stree = self.insert_node(node.left_stree, value)
        else:
            node.right_stree = self.insert_node(node.right_stree, value)

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
            temp = self.get_min_val(node.right_stree)
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

    # Get the height of the node

    def update_balance(self, curr_node):
        if not curr_node:
            return 0
        return self.update_height(curr_node.left_stree) - self.update_height(curr_node.right_stree)

    def get_min_val(self, curr_node):
        if curr_node is None or curr_node.left_stree is None:
            return curr_node
        return self.get_min_val(curr_node.left_stree)

    def display_avl_tree(self, currPtr, indent, last):
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.root)
            self.display_avl_tree(currPtr.left_stree, indent, False)
            self.display_avl_tree(currPtr.right_stree, indent, True)


if __name__ == '__main__':
    nums = [46, 27, 58, 14, 78, 36]
    myTree = AVLTree()
    full_root = None
    for num in nums:
        full_root = myTree.insert_node(full_root, num)
    myTree.display_avl_tree(full_root, "", True)
    key = 14
    root = myTree.delete_node(full_root, key)
    post_arr = full_root.post_order_traversal()
    pre_arr = full_root.pre_order_traversal()
    print('===' * 60)
    print('Post Order Arr: \n\t'.format(post_arr))
    print('Pre Order Arr: \n\t{}'.format(pre_arr))
    print('===' * 60)
    print("After Deletion: ")
    myTree.display_avl_tree(full_root, "", True)
