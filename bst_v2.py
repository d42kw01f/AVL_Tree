import sys


# Create a tree node
class CreateTree:
    def __init__(self, data):
        self.root = data
        self.left_stree = None
        self.right_stree = None


class AVLTree(CreateTree):
    def __init__(self, data):
        super().__init__(data)
        self.height = 1

    # Function to insert a node
    def insert_child(self, node, val):
        if not node:
            return AVLTree(val)
        elif val < node.root:
            node.left_stree = self.insert_child(node.left_stree, val)
        else:
            node.right_stree = self.insert_child(node.right_stree, val)

        node.height = 1 + max(self.update_height(node.left_stree),
                              self.update_height(node.right_stree))

        # Update the balance factor and balance the tree
        balance_factor = self.update_balance(node)
        if balance_factor > 1:
            if val < node.left_stree.root:
                return self.r_rotate(node)
            else:
                node.left_stree = self.l_rotate(node.left_stree)
                return self.r_rotate(node)

        if balance_factor < -1:
            if val > node.right_stree.root:
                return self.l_rotate(node)
            else:
                node.right_stree = self.r_rotate(node.right_stree)
                return self.l_rotate(node)

        return node

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.root:
            root.left_stree = self.delete_node(root.left_stree, key)
        elif key > root.root:
            root.right_stree = self.delete_node(root.right_stree, key)
        else:
            if root.left_stree is None:
                temp = root.right_stree
                root = None
                return temp
            elif root.right_stree is None:
                temp = root.left_stree
                root = None
                return temp
            temp = self.min_node_value(root.right_stree)
            root.root = temp.root
            root.right_stree = self.delete_node(root.right_stree,
                                                temp.root)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.update_height(root.left_stree),
                              self.update_height(root.right_stree))

        balanceFactor = self.update_balance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.update_balance(root.left_stree) >= 0:
                return self.r_rotate(root)
            else:
                root.left_stree = self.l_rotate(root.left_stree)
                return self.r_rotate(root)
        if balanceFactor < -1:
            if self.update_balance(root.right_stree) <= 0:
                return self.l_rotate(root)
            else:
                root.right_stree = self.r_rotate(root.right_stree)
                return self.l_rotate(root)
        return root

    # Function to perform left rotation
    def l_rotate(self, z):
        y = z.right_stree
        T2 = y.left_stree
        y.left_stree = z
        z.right_stree = T2
        z.height_stree = 1 + max(self.update_height(z.left_stree), self.update_height(z.right_stree))
        y.height = 1 + max(self.update_height(y.left_stree), self.update_height(y.right_stree))
        return y

    # Function to perform right rotation
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

    # Get the height of the node
    @staticmethod
    def update_height(element):
        if not element:
            return 0
        return element.height

    # Get balance factore of the node
    def update_balance(self, element):
        if not element:
            return 0
        return self.update_height(element.left_stree) - self.update_height(element.right_stree)

    def min_node_value(self, element):
        if element is None or element.left is None:
            return element
        return self.min_node_value(element.left)

    def preOrder(self, element):
        if not element:
            return
        print("{0} ".format(element.key), end="")
        self.preOrder(element.left)
        self.preOrder(element.right)

    # Print the tree
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


# myTree = AVLTree()
root = None
# nums = [33, 13, 52, 9, 21, 61, 8, 11]
nums = [33, 13, 323, 5, 52, 9, 673, 123, 42, 21, 61, 8, 11, 62, 63]
myTree = AVLTree(nums[0])
for num in nums[1:]:
    root = myTree.insert_child(root, num)
myTree.printHelper(root, "", True)
key = 11
root = myTree.delete_node(root, key)
print("After Deletion: ")
myTree.printHelper(root, "", True)
