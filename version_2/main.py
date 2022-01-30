import os
import avl


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
    while True:
        try:
            arr_elem = int(input('\x1b[6;30;42m' + '---> Number of Elements in the Array:' + '\x1b[0m' + ' '))
            user_int = [int(input(f"\tEnter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]
            break
        except ValueError:
            print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
    print(
        '\33[93m' + '\nNOTE: AVL only works with distinct values. Thus, Duplicates values. They will be automatically removed.' + '\33[0m')
    return list(dict.fromkeys(user_int))


def program_exit():
    print('\33[92m' + '===' * 30 + '\33[0m')
    try:
        print('\t\t\t\U0001F600 Thanks for using this\n\t\t\tLive Long and Prosper \U0001F596')
    except:
        print('Thanks')
    print('\33[92m' + '===' * 30 + '\33[0m')
    exit()


def user_options():
    clear_console()
    print('''  
░█████╗░██╗░░░██╗██╗░░░░░░░░░░░████████╗██████╗░███████╗███████╗
██╔══██╗██║░░░██║██║░░░░░░░░░░░╚══██╔══╝██╔══██╗██╔════╝██╔════╝
███████║╚██╗░██╔╝██║░░░░░█████╗░░░██║░░░██████╔╝█████╗░░█████╗░░
██╔══██║░╚████╔╝░██║░░░░░╚════╝░░░██║░░░██╔══██╗██╔══╝░░██╔══╝░░
██║░░██║░░╚██╔╝░░███████╗░░░░░░░░░██║░░░██║░░██║███████╗███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝
                                        name: Dakshitha Perera
                                        ecu ID - 10519381
    ''')
    print('\33[94m' + '===' * 30 + '\33[0m')
    print(
        '1.) Per-load a sequence of integers to build a BST\n'
        '2.) Manually enter integer values/keys, one by one to build a BST\n'
        '3.) Exit')
    print('\33[94m' + '===' * 30 + '\33[0m')

    try:
        user_choice = int(input('\33[93m' + 'Enter your option here: ' + '\33[0m'))
    except ValueError:
        print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
        input('\tPress Enter to continue...')
        return user_options()
    if user_choice == 1:
        user_arr = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]
    elif user_choice == 2:
        user_arr = user_prompt()
    else:
        program_exit()
    # noinspection PyUnboundLocalVariable
    return user_arr


def input_int(verb):
    while True:
        try:
            the_int = int(input('\33[93m' + f'Enter {verb} Value: ' + '\33[0m'))
            return the_int
        except ValueError:
            print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')


def main_menu(Tree, obj_avl):
    clear_console()
    while True:
        print('\33[94m' + '===' * 30 + '\33[0m')
        print("""
        1.\tDisplay the AVL tree, showing the height and balance factor for each node.
        2.\tPrint the pre-order, in-order and post-order traversal sequences of the AVL tree
        3.\tPrint all leaf nodes of the AVL tree, and all non-leaf nodes
        4.\tInsert a new integer key into the AVL tree
        5.\tDelete an integer key from the AVL tree
        6.\tExit
        """)
        print('\33[94m' + '===' * 30 + '\33[0m')
        try:
            menu_choice = int(input('Enter your option here: '))
            break
        except ValueError:
            print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
            input('\tPress Enter to continue...')
    # noinspection PyUnboundLocalVariable
    print('\n\t\t\t\t\U0001F648 RESULTS:')
    print('\33[92m' + '===' * 30 + '\33[0m')
    match menu_choice:
        case 1:
            Tree.printHelper(obj_avl, '', True)

        case 2:
            per_order = obj_avl.pre_order_traversal()
            in_order = obj_avl.in_order_traversal()
            post_order = obj_avl.post_order_traversal()
            print('per-order traversal : \n\t{}'.format(per_order))
            print('in-order traversal : \n\t{}'.format(in_order))
            print('post-order traversal : \n\t{}'.format(post_order))

        case 3:
            print('\33[92m' + '===' * 30 + '\33[0m')
            # TODO: Printing Leaf and Non-Leaf Nodes
            print('Under Construction...')
            print('\33[92m' + '===' * 30 + '\33[0m')

        case 4:
            insert_node = input_int(verb='Insert')
            search_results = obj_avl.search_elements(insert_node)
            if search_results is None:
                obj_avl = Tree.insert_child(obj_avl, insert_node)
                Tree.printHelper(obj_avl, '', True)
            else:
                print(f'\t\33[91m\U0001F641 SORRY: I cannot insert it\n '
                      f'\tCuz, {insert_node} node is already in the AVL Tree')

        case 5:
            del_node = input_int(verb='Delete')
            search_results = obj_avl.search_elements(del_node)
            if search_results:
                obj_avl = Tree.delete_node(obj_avl, del_node)
                Tree.printHelper(obj_avl, '', True)
            else:
                print(f'\t\33[91m\U0001F641 SORRY: I could not find {del_node} node in the AVL Tree')

        case 6:
            program_exit()

    print('\33[92m' + '===' * 30 + '\33[0m')


if __name__ == '__main__':
    seq_int = user_options()
    AVLTree = avl.AVLTree()
    print()
    print('===' * 30)
    print('sequence of integers for AVL Tree would be: \n\t{}'.format(seq_int))
    print('===' * 30)
    input('\nPress Enter to continue...')
    full_avl = construct_bst(AVLTree, seq_int)
    while True:
        main_menu(AVLTree, full_avl)
        input('\n\tPress Enter to continue...')
