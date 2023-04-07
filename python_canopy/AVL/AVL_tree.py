from dataclasses import dataclass
from queue import Queue
import random
from typing import Any, Optional


@dataclass
class Node:
    value: int  # key or value, is what we are checking for balance, can be int or Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None
    height: int = 0  # height of the node// new addition

    def __str__(self) -> str:
        return f"Node({self.value})"

    def __repr__(self) -> str:
        return f"Node({self.value})"


@dataclass
class AVLTree:
    # init the root of the tree
    root: Optional[Node] = None

    def insert(self, value: int) -> None:
        """ Inserts a value into the tree.

            Args:
                value (int): The value to insert.
        """

        new_node = Node(value=value)
        parent: Optional[Node] = None
        current: Optional[Node] = self.root

        while current is not None:
            parent = current
            # if the value is less than the current node's value, go to the left subtree
            if new_node.value < current.value:
                current = current.left
            # if the value is greater than the current node's value, go to the right subtree
            elif new_node.value > current.value:
                current = current.right
            # if the value is equal to the current node's value, return None
            else:
                print("The value already exists in the tree.")

        new_node.parent = parent
        # if the tree is empty, set the new node as the root
        if parent is None:
            self.root = new_node
        else:
            # if the value is less than the parent's value, set the new node as the left child
            if new_node.value < parent.value:
                parent.left = new_node
            # if the value is greater than the parent's value, set the new node as the right child
            else:
                parent.right = new_node

            if not (parent.left and parent.right):
                self._insert_fixup(new_node=new_node)

    # Delete function using the transplate method and the search method
    def search(self, value: int) -> Optional[Node]:
        """Searches for a value in the tree and returns the node with the value.

        Args:
            value (int): The value to search for.

        Returns:
            Optional[Node]: The node with the value.
        """
        # if the tree is empty, return None
        if self.root is None:
            return None

        # otherwise, call the private method
        else:
            return self._search(value=value)

    def _search(self, value: int) -> Optional[Node]:
        """Private method to search for a value in the tree and return the node with the value.

        Args:
            value (int): The value to search for.

        Returns:
            Optional[Node]: The node with the value.
        """
        current = self.root

        # while the current node is not None
        while current is not None:
            # case 1: if the value is less than the current node's value, search the left subtree
            if value < current.value:
                current = current.left

            # case 2: if the value is greater than the current node's value, search the right subtree
            elif value > current.value:
                current = current.right

            # case 3: if the value is equal to the current node's value, return the node
            else:
                return current

        # if the value is not found, return None
        return None

    def delete(self, value: int) -> None:
        """Deletes a node from the tree.

        Args:
            value (int): The value to delete.
        """
        # if the tree is empty, return None
        if self.root and (deleting_node := self._search(value=value)):

            # case 1: no children
            if deleting_node.left is None and deleting_node.right is None:
                self._transplate(u=deleting_node, v=None)

    # -----------------------------------// Auxiliary functions //-----------------------------------#
    def _transplate(self, u: Node, v: Optional[Node]) -> None:
        """Transplate u for v.

        Args:
            u (Node): The node to transplate.
            v (Node): The node to transplate for.
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    @property
    def empty(self) -> bool:
        """ Return True if the tree is empty"""
        return self.root is None

    @staticmethod  # staticmethod() é uma função que não precisa de self
    def get_leftmost(node: Node) -> Node:
        """Gets the leftmost node of a subtree.

        Args:
            node (Node): The root of the subtree.

        Returns:
            Node: The leftmost node of the subtree.
        """
        while node.left is not None:
            node = node.left
        return node

    @staticmethod
    def get_rightmost(node: Node) -> Node:
        """Gets the rightmost node of a subtree.

        Args:
            node (Node): The root of the subtree.

        Returns:
            Node: The rightmost node of the subtree.
        """
        while node.right is not None:
            node = node.right
        return node

    @staticmethod
    def get_successor(node: Node) -> Optional[Node]:
        """Gets the successor of a node.

        Args:
            node (Node): The node to get the successor of.

        Returns:
            Node: The successor of the node.
        """
        # case 1: if the node has a right child, return the leftmost node of the right subtree
        if node.right is not None:
            return AVLTree.get_leftmost(node=node.right)
        # case 2: right child is empty
        parent = node.parent
        while parent and (node == parent.right):
            node = parent
            parent = parent.parent
        return parent

    @staticmethod
    def get_predecessor(node: Node) -> Optional[Node]:
        """Gets the predecessor of a node.

        Args:
            node (Node): The node to get the predecessor of.

        Returns:
            Node: The predecessor of the node.
        """
        # case 1: if the node has a left child, return the rightmost node of the left subtree
        if node.left is not None:
            return AVLTree.get_rightmost(node=node.left)
        # case 2: left child is empty
        parent = node.parent
        while parent and (node == parent.left):
            node = parent
            parent = parent.parent
        return parent

    @staticmethod
    def get_height(node: Optional[Node]) -> int:
        """ Return the height of the node
        
        Args:
            Optional[Node]: the node to get the height of
        
        Returns:
            int: the height of the node
        """
        if node is not None:
            return node.height
        # if the node is None, return -1
        return -1

    def _get_balance_factor(self, node: Optional[Node]) -> int:
        """ Return the balance factor of the node
        
        Args:
            Optional[Node]: the node to get the balance factor of
        
        Returns:
            int: the balance factor of the node
        """
        # if the node is not None, return the height of the left subtree - the height of the right subtree
        if node is not None:
            return self.get_height(node.left) - self.get_height(node.right)
        # if the node is None, return 0
        return -1

    def _left_rotate(self, node_x: Node) -> None:
        """Left rotate the subtree rooted at node x.
         
        Args:
            node_x (Node): The root of the subtree to left rotate.
        """
        node_y = node_x.right  # Set node y
        if node_y:
            # Turn node y's subtree into node x's subtree
            node_x.right = node_y.left
            if node_y.left:
                node_y.left.parent = node_x
            node_y.parent = node_x.parent

            # If node's parent is a Leaf, node y becomes the new root.
            if node_x.parent is None:
                self.root = node_y
            # Otherwise, update node x's parent.
            elif node_x == node_x.parent.left:
                node_x.parent.left = node_y
            else:
                node_x.parent.right = node_y

            node_y.left = node_x
            node_x.parent = node_y

            node_x.height = 1 + max(self.get_height(node_x.left),
                                    self.get_height(node_x.right))
            node_y.height = 1 + max(self.get_height(node_y.left),
                                    self.get_height(node_y.right))

    def _right_rotate(self, node_x: Node) -> None:
        """ Right rotate the subtree rooted at node x.

            Args:
                node_x (Node): The root of the subtree to right rotate.
        """
        node_y = node_x.left  # Set node y
        if node_y:
            # Turn node y's subtree into node x's subtree
            node_x.left = node_y.right
            if node_y.right:
                node_y.right.parent = node_x
            node_y.parent = node_x.parent

            # If node's parent is a Leaf, node y becomes the new root.
            if node_x.parent is None:
                self.root = node_y
            # Otherwise, update node x's parent.
            elif node_x == node_x.parent.right:
                node_x.parent.right = node_y
            else:
                node_x.parent.left = node_y

            node_y.right = node_x
            node_x.parent = node_y

            node_x.height = 1 + max(self.get_height(node_x.left),
                                    self.get_height(node_x.right))
            node_y.height = 1 + max(self.get_height(node_y.left),
                                    self.get_height(node_y.right))

    def _insert_fixup(self, new_node: Node) -> None:
        parent = new_node.parent

        # iterate until the parent is not None
        while parent is not None:
            # parent height is 1 + the max of the heights of the children
            parent.height = 1 + max(self.get_height(parent.left),
                                    self.get_height(parent.right))

            grandparent = parent.parent

            if grandparent is not None:
                # if the balance factor of the grandparent is greater than 1, we have an imbalance
                if self._get_balance_factor(grandparent) > 1:
                    # left left case
                    if self._get_balance_factor(parent) >= 0:
                        self._right_rotate(grandparent)

                    # left right case
                    elif self._get_balance_factor(parent) < 0:
                        self._left_rotate(parent)
                        self._right_rotate(grandparent)

                    break
                # if the balance factor of the grandparent is less than -1, we have an imbalance
                elif self._get_balance_factor(grandparent) < -1:
                    # right right case
                    if self._get_balance_factor(parent) <= 0:
                        self._left_rotate(grandparent)

                    # right left case
                    elif self._get_balance_factor(parent) > 0:
                        self._right_rotate(parent)
                        self._left_rotate(grandparent)

                    break

            parent = parent.parent

    def _delete_no_child(self, deleting_node: Node) -> None:
        """ Delete a node with no children
        
        Args:
            deleting_node: the node to delete
        """
        # if the node to delete is the root, set the root to None
        parent = deleting_node.parent
        self._transplate(u=deleting_node, v=None)
        if parent is not None:
            self._delete_fixup(fixing_node=parent)

    def _delete_one_child(self, deleting_node: Node) -> None:
        """ Delete a node with one child
        
        Args:
            deleting_node: the node to delete
        """
        # if the node to delete is the root, set the root to the child
        parent = deleting_node.parent
        if deleting_node.left is not None:
            self._transplate(u=deleting_node, v=deleting_node.left)
        else:
            self._transplate(u=deleting_node, v=deleting_node.right)
        if parent is not None:
            self._delete_fixup(fixing_node=parent)

    def _delete_fixup(self, fixing_node: Node) -> None:
        """ Fix the tree after a deletion
        
        Args:
            fixing_node: the node to start fixing from
        """
        # iterate until the fixing node is not None
        while fixing_node is not None:
            # fixing node height is 1 + the max of the heights of the children
            fixing_node.height = 1 + max(self.get_height(fixing_node.left),
                                         self.get_height(fixing_node.right))

            # if the balance factor of the fixing node is greater than 1, we have an imbalance
            if self._get_balance_factor(fixing_node) > 1:
                # left left case
                if self._get_balance_factor(fixing_node.left) >= 0:
                    self._right_rotate(fixing_node)

                # left right case
                elif self._get_balance_factor(fixing_node.left) < 0:
                    self._left_rotate(fixing_node.left)  # type: ignore
                    self._right_rotate(fixing_node)

            # if the balance factor of the fixing node is less than -1, we have an imbalance
            elif self._get_balance_factor(fixing_node) < -1:
                # right right case
                if self._get_balance_factor(fixing_node.right) <= 0:
                    self._left_rotate(fixing_node)

                # right left case
                elif self._get_balance_factor(fixing_node.right) > 0:
                    self._right_rotate(fixing_node.right)  # type: ignore
                    self._left_rotate(fixing_node)

            fixing_node = fixing_node.parent  # type: ignore

    # -----------------------------------// Print functions //-----------------------------------#
    ## Function to print level order traversal of tree
    def print_level_order(self) -> None:
        height = self.get_height(self.root)
        print('Height of tree: {}'.format(height))
        # the height of the tree is the number of levels but we start counting at 0
        for i in range(height + 1):
            self._print_given_level(self.root, i)
            print()

    def _print_given_level(self, root: Optional[Node], level: int) -> None:
        # base case
        if root is None:
            return
        # if the current level is 0, print the node
        if level == 0:
            print(root.value, end=' ')
        # if the current level is greater than 0, print the children
        elif level >= 1:
            self._print_given_level(root.left, level - 1)
            self._print_given_level(root.right, level - 1)

    def fill_tree_random(self, size: int, max_value: int) -> None:
        """ Fill the tree with random values
        
        Args:
            size: the number of values to add to the tree
            max_value: the maximum value to add to the tree
        """
        # add random values to the tree
        for _ in range(size):
            self.insert(random.randint(0, max_value))

    def fill_tree_ordered(self, size: int) -> None:
        """ Fill the tree with ordered values
        
        Args:
            size: the number of values to add to the tree
        """
        # add ordered values to the tree
        for i in range(size):
            self.insert(i)

    def print_tree_inorder(self) -> None:
        """ Print the tree in order """
        self._print_tree('inorder')

    def print_tree_preorder(self) -> None:
        """ Print the tree in preorder """
        self._print_tree('preorder')

    def print_tree_postorder(self) -> None:
        """ Print the tree in postorder """
        self._print_tree('postorder')

    def _print_tree(self, traversal_type: str = 'inorder') -> None:
        """ Print the tree
        
        Args:
            traversal_type: the type of traversal to use
        """
        # if the tree is empty, print that the tree is empty
        if self.empty:
            print('Tree is empty')
            return

        # otherwise print the tree in the specified traversal
        if traversal_type == 'inorder':
            self._inorder(self.root)
        elif traversal_type == 'preorder':
            self._preorder(self.root)
        elif traversal_type == 'postorder':
            self._postorder(self.root)
        else:
            print('Traversal type ' + str(traversal_type) +
                  ' is not supported')
            return

        print()

    def _inorder(self, node: Optional[Node]) -> None:
        """ Print the tree in order
        
        Args:
            Optional[Node]: the node to start printing from
        """
        # if the node is None, return
        if node is None:
            return

        # otherwise print the left subtree, the node, and the right subtree
        self._inorder(node.left)
        print(node.value, end=' ')
        self._inorder(node.right)

    def _preorder(self, node: Optional[Node]) -> None:
        """ Print the tree in preorder
        
        Args:
            Optional[Node]: the node to start printing from
        """
        # if the node is None, return
        if node is None:
            return

        # otherwise print the node, the left subtree, and the right subtree
        print(node.value, end=' ')
        self._preorder(node.left)
        self._preorder(node.right)

    def _postorder(self, node: Optional[Node]) -> None:
        """ Print the tree in postorder
        
        Args:
            Optional[Node]: the node to start printing from
        """
        # if the node is None, return
        if node is None:
            return

        # otherwise print the left subtree, the right subtree, and the node
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.value, end=' ')


import graphviz


class AVLTreeGraph(AVLTree):
    """ AVL Tree Graph Class """

    def __init__(self):
        """ Initialize the AVL Tree Graph """
        super().__init__()

    def _graphviz(self, node: Optional[Node], graph: graphviz.Digraph) -> None:
        """ Graphviz function to create the graph
        
        Args:
            node: the node to add to the graph
            graph: the graph to add the node to
        """
        # if the node is None, return
        if node is None:
            return

        # otherwise add the node to the graph
        graph.node(str(node.value), str(node.value))

        # if the node has a left child, add the edge to the graph
        if node.left is not None:
            graph.edge(str(node.value), str(node.left.value))

        # if the node has a right child, add the edge to the graph
        if node.right is not None:
            graph.edge(str(node.value), str(node.right.value))

        # recursively call the function on the left and right subtrees
        self._graphviz(node.left, graph)
        self._graphviz(node.right, graph)

    def graphviz(self) -> graphviz.Digraph:
        """ Graphviz function to create the graph
        
        Returns:
            graphviz.Digraph: the graph
        """
        # create the graph
        graph = graphviz.Digraph()

        # call the graphviz function
        self._graphviz(self.root, graph)

        # return the graph
        return graph


# test the AVL tree
# create an AVL tree
tree = AVLTree()

# list
lst = [
    59, 16, 9, 8, 0, 6, 15, 41, 27, 23, 19, 17, 21, 40, 39, 32, 38, 53, 49, 47,
    46, 43, 48, 50, 55, 95, 72, 69, 64, 61, 65, 71, 89, 76, 73, 74, 85, 93, 96
]

# fill the tree with the list
for i in lst:
    tree.insert(i)

# fill the tree with random values
#tree.fill_tree_random(50, 100)

# fill the tree with ordered values
#tree.fill_tree_ordered(50)

# print the tree in order
print('Inorder:')
tree.print_tree_inorder()

# print the tree in preorder
print('Preorder:')
tree.print_tree_preorder()

# print the tree in postorder
print('Postorder:')
tree.print_tree_postorder()

# print the tree in level order
print('Level order:')
tree.print_level_order()

# create avl tree graph
avl_tree_graph = AVLTreeGraph()

# fill the tree with the list
for i in lst:
    avl_tree_graph.insert(i)

# render the graph
graph = avl_tree_graph.graphviz()

# render the graph
graph.render(filename='avl_tree_graph', format='png')
