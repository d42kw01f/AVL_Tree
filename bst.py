import os


# This parent class allows to organize codes specially lin the main script which uses BTS and AVL.
class CreateTree:
    def __init__(self, data):
        self.root = data
        self.left_stree = None
        self.right_stree = None


class BinarySearchTree(CreateTree):
    def __init__(self, data):
        super().__init__(data)  # Initializing the tree from super class

    def insert_child(self, key):
        if self.root is key:  # Check if data tries to add is already in the BST. If it is the case return nothing
            return

        if self.root > key:  # Check if the root is greater than data
            if self.left_stree:  # If it is the case use, Check left node has any values by calling recursive methods.
                self.left_stree.insert_child(key)
            else:  # Else simply add data to the left_node.
                self.left_stree = BinarySearchTree(key)

        else:  # If data is greater than the root add data to right node like adding data to the left node.
            if self.right_stree:
                self.right_stree.insert_child(key)
            else:
                self.right_stree = BinarySearchTree(key)

    # This is per order traversal function ===> Root => Left => Right
    def _per_order_traversal(self):
        tree_nodes = [self.root]  # Append root to the array

        if self.left_stree:  # If left node exists, Go to it.
            tree_nodes += self.left_stree._per_order_traversal()
        if self.right_stree:  # If Right tree exist, Go to it
            tree_nodes += self.right_stree._per_order_traversal()

        return tree_nodes

    # This function searches any given value in the node and return its object.
    def search_elements(self, val):
        if self.root is val:  # Check if root is the searching value.
            return self  # Then return its object
        if self.root > val:  # If searching value is less than the root, search left subtree
            if self.left_stree:
                return self.left_stree.search_elements(val)
            else:
                return None
        if self.root < val:  # if Searching value is grater than the root, search right subtree
            if self.right_stree:
                return self.right_stree.search_elements(val)
            else:
                return None

    # This function calculates the depth of the subtree rotted at N.
    def sub_tree_depth(self, given_node):
        tree_obj = self.search_elements(given_node)  # Search the given_node using and return its object
        depth_n_node = tree_obj.depth()  # calculating the depth of the subtree which rooted at N
        return depth_n_node

    # This function calculates the depth of a given tree
    def depth(self):
        left_depth = self.left_stree.depth() if self.left_stree else 0
        right_depth = self.right_stree.depth() if self.right_stree else 0
        return max(left_depth, right_depth) + 1

    # This is per order traversal function ===> Left => Right => Root
    def post_order_traversal(self):
        tree_nodes = []

        if self.left_stree:  # If left exit, travel
            tree_nodes += self.left_stree.post_order_traversal()
        if self.right_stree:  # if right exist, travel
            tree_nodes += self.right_stree.post_order_traversal()
        tree_nodes.append(self.root)  # append the root to the array

        return tree_nodes


# This function create the Binary Search Tree.
def construct_bst(given_arr):
    root = BinarySearchTree(given_arr[0])  # Create and Object of BinarySearchTree
    for i in range(1, len(given_arr)):
        root.insert_child(given_arr[i])  # Insert nodes to the BST one by one
    return root


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def user_prompt():
    arr_elem = int(input('\x1b[6;30;42m' + '---> Number of Elements in the Array:' + '\x1b[0m' + ' '))
    user_int = [int(input(f"\tEnter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]
    print(
        '\33[93m' + '\nNOTE: BST only works with distinct values. Thus, Duplicates values. They will be automatically removed.' + '\33[0m')
    return list(dict.fromkeys(user_int))


def user_options():
    clear_console()
    print(
        '1.) Per-load a sequence of integers to build a BST\n2.) Manually enter integer values/keys, one by one to build a BST\n3.) Exit')
    try:
        user_choice = int(input('Enter your option here: '))
    except ValueError:
        print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
        input('\tEnter any key to continue...')
        user_options()
    if user_choice == 1:
        user_arr = [54, 80, 64, 19, 34, 78, 22, 13, 20, 102, 91, 44, 84, 50, 46, 47, 49, 45]
    elif user_choice == 2:
        user_arr = user_prompt()
    else:
        exit()
    return user_arr


def construct_bst(given_arr):
    root = BinarySearchTree(given_arr[0])  # Create and Object of BinarySearchTree
    for i in range(1, len(given_arr)):
        root.insert_child(given_arr[i])  # Insert nodes to the BST one by one
    return root


if __name__ == '__main__':
    seq_int = user_options()
    print('sequence of integers for BST would be: \n\t{}'.format(seq_int))
    full_bst = construct_bst(seq_int)
    depth = full_bst.sub_tree_depth(54)
    print(depth)