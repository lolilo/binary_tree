# A binary tree has the following attributes:

# class BinaryTreeNode
#     get_left() => BinaryTreeNode
#     set_left(BinaryTreeNode)
#     get_right() => BinaryTreeNode
#     set_right(BinaryTreeNode)
#     get_value() => int
#     set_value(int)

# The value can be an arbitrary number, and the get_left and get_right methods
# can return a None.

class BinaryTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node

    def get_value(self):
        return self.value

    def set_value(self, number):
        self.value = number

def depth_first_traversal(node):
    print node.value,
    # two children
    if (node.get_left() and node.get_right()):
        depth_first_traversal(node.get_left())
        depth_first_traversal(node.get_right())
    
    # one child
    elif node.get_left():
        depth_first_traversal(node.get_left())


def test(node):
    if node == None:
        return
    
    print node.value,
    test(node.get_left())
    test(node.get_right())

# The easiest way to do a depth-first traversal is with a recursive function. It
# should print the value of the current node, then call itself on the left, then
# right node in order.


# def depth_first_traversal(node):
#     # two children
#     if bool(node.get_left()) and bool(node.get_right()):
#         print node.value,
#         print depth_first_traversal(node.get_left()),
#         print depth_first_traversal(node.get_right()),
#         # return 'dummy'
#     # one child
#     elif bool(node.get_left()):
#         print node.value,
#         print depth_first_traversal(node.get_left()),
#         # return 'dummy'
#     # no children
#     else: 
#         print node.value # this returns None...how to circumvent? 


# FUNCTIONS RETURN STUFF AND YOU PRINT THE RETURNED STUFF.
# WAIT. NO. THIS FUNCTION JUST NEEDS TO PRINT. DOESN'T NEED TO RETURN SHIT. 
# THE TEST FILE WILL ACCOUNT FOR THIS AND READ THE PRINTED NUMBERS ON THE TERMINAL.
# FUCKING HELL. 

root = BinaryTreeNode(0)
left = BinaryTreeNode(1)
right = BinaryTreeNode(4)
l_left = BinaryTreeNode(2)
l_right = BinaryTreeNode(3)
r_left = BinaryTreeNode(5)
r_right = BinaryTreeNode(6)

root.set_left(left)
root.set_right(right)
left.set_left(l_left)
left.set_right(l_right)
right.set_left(r_left)
right.set_right(r_right)


expected = "0 1 2 3 4 5 6"
print "Your output", 
# depth_first_traversal(root)
test(root)
print "\nExpected output", expected
