# http://www.laurentluce.com/posts/binary-search-tree-library-in-python/

class Node: 
    # tree node: left and right child + data that can be any object
    def __init__(self, data):
        # node constructor
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # insert new node with data
        # what does this mean? data < self.data?
        # this creates an ordered tree with "smaller" data on the left
        # "larger" data to the right
        
        # print """
        # """
        # print 'data is', data, ', self.data is', self.data
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                # self-reference
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else: 
                self.right.insert(data)

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                # returns None if not in tree
                return None, None
            # continue seraching if more nodes are present
            return self.left.lookup(data,self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else: 
            # if data = self.data, return self/current Node and parent Node
            return self, parent

    def children_count(self):
        if node is None:
            return None
        count = 0
        if self.left: 
            count += 1
        if self.right:
            count += 1
        return count

    def delete(self, data):
        # locate position of self
        node, parent = self.lookup(data)
        # if not exists in the binary tree
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # if node has no children, simply delete it
                if parent.left is node:
                    parent.left = None
                else: 
                    parent.right = None
                # could I just delete the node without setting it to None? 
                del node
            
            elif children_count == 1:
                # if node has one child, replace node by its child
                if node.left: 
                    n = node.left
                else: 
                    n = node.right
                if parent: 
                    # move child node value up one level in the tree
                    if parent.left is node: 
                        parent.left = n 
                    else: 
                        parent.right = n

            else:
                # if node has two children, find its successor
                parent = node # each node can only have a single parent
                # at this point, parent object is no longer referenced. parent and node are the same.
                # parent becomes a somewhat uninformative variable name 
                # parent is a variable we use and reassign by convenience of its existence
                # parent is actually the parent of the sucessor, successor's parent

                successor = node.right
                while successor.left:
                    # what is the point of parent = node earlier, then? 
                    parent = successor
                    sucessor = successor.left
                # replace node data by its successor data
                # by virtue of the sorted binary tree, it will be a smaller number than parent.data
                node.data = successor.data
                # fix successor's parent's child
                if parent.left == successor: 
                    parent.left = successor.right
                else: 
                    parent.right = successor.right


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

node, parent = root.lookup(6)
print node.data, parent.data

