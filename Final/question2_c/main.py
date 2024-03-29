import avl
import os


# This function create the Binary Search Tree.
def construct_bst(tree_obj, given_arr):
    Tree = None
    for idx, num in enumerate(given_arr):
        Tree = tree_obj.insert_child(Tree, num)  # Insert nodes to the BST one by one
    return Tree


# This function will clear the terminal once it's called.
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
        '1.) Per-load a sequence of integers to build an AVL Tree\n'
        '2.) Manually enter integer values/keys, one by one to build an AVL Tree\n'
        '3.) Exit')
    try:
        user_choice = int(input('Enter your option here: '))
    except ValueError:
        print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
        input('\tPress Enter to continue...')
        return user_options()
    if user_choice == 1:
        user_arr = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]
    elif user_choice == 2:
        user_arr = user_prompt()
    else:
        exit()
    # noinspection PyUnboundLocalVariable
    return user_arr


def input_int(verb):
    try:
        the_int = int(input('Enter {} Value: '.format(verb)))
    except ValueError:
        print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
    # noinspection PyUnboundLocalVariable
    return the_int


def main_menu(Tree, obj_avl):
    clear_console()
    print(""" 
    1.\tDisplay the AVL tree, showing the height and balance factor for each node.
    2.\tPrint the pre-order, in-order and post-order traversal sequences of the AVL tree
    3.\tPrint all leaf nodes of the AVL tree, and all non-leaf nodes
    4.\tInsert a new integer key into the AVL tree
    5.\tDelete an integer key from the AVL tree
    6.\tExit
    """)
    try:
        menu_choice = int(input('Enter your option here: '))
    except ValueError:
        print('\n' + '\33[41m' + '\tERROR: Input is invalid!!!' + '\33[0m')
        input('\tPress Enter to continue...')
        menu_choice = int(input('\nEnter your option here: '))
    # noinspection PyUnboundLocalVariable
    match menu_choice:
        case 1:
            print('===' * 30)
            Tree.printHelper(obj_avl, '', True)
            print('===' * 30)

        case 2:
            per_order = obj_avl.pre_order_traversal()
            in_order = obj_avl.in_order_traversal()
            post_order = obj_avl.post_order_traversal()
            print('===' * 30)
            print('per-order traversal : \n\t{}'.format(per_order))
            print('in-order traversal : \n\t{}'.format(in_order))
            print('post-order traversal : \n\t{}'.format(post_order))
            print('===' * 30)

        case 3:
            print('===' * 30)
            # TODO: Printing Leaf and Non-Leaf Nodes
            print('Under Construction...')
            print('===' * 30)

        case 4:
            print('===' * 30)
            insert_node = input_int(verb='Insert')
            obj_avl = Tree.insert_child(obj_avl, insert_node)
            Tree.printHelper(obj_avl, '', True)
            print('===' * 30)

        case 5:
            print('===' * 30)
            del_node = input_int(verb='Delete')
            obj_avl = Tree.delete_node(obj_avl, del_node)
            Tree.printHelper(obj_avl, '', True)
            print('===' * 30)

        case 6:
            exit()


if __name__ == '__main__':
    # arr = [46, 27, 58, 14, 78, 36]
    seq_int = user_options()
    AVLTree = avl.AVLTree()
    #
    print()
    print('===' * 30)
    print('sequence of integers for BST would be: \n\t{}'.format(seq_int))
    print('===' * 30)
    input('\nPress Enter to continue...')
    full_avl = construct_bst(AVLTree, seq_int)
    while True:
        main_menu(AVLTree, full_avl)
        input('\n\tPress Enter to continue...')
