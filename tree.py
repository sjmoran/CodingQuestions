
class BinaryTree():

    def __init__(self, root):

        self.left = None
        self.right = None
        self.root = root

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_node_value(self, value):
        self.root = value

    def get_node_value(self):
        return self.root

    def insert_right(self, new_node):
        if self.right == None:
            self.right = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.right = self.right
            self.right = tree

    def insert_left(self, new_node):
        if self.left == None:
            self.left = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.left = self.left
            self.left = tree


def print_leaves(tree):

    if tree != None:
        if ((tree.get_left_child() == None) and (tree.get_right_child() == None)):
            print tree.get_node_value()
        else:
            print_leaves(tree.get_left_child())
            print_leaves(tree.get_right_child())


def print_tree(tree):
    if tree != None:
        print_tree(tree.get_left_child())
        print(tree.get_node_value())
        print_tree(tree.get_right_child())


def test():

    my_tree = BinaryTree("1")
    my_tree.insert_left("4")
    my_tree.insert_left("2")
    my_tree.insert_right("6")
    my_tree.insert_right("5")
    my_tree.insert_right("3")

    print my_tree
    print_leaves(my_tree)


test()
