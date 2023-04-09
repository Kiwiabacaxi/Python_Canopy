import enum
from typing import Any, Iterator, Optional, Union, Iterable
from dataclasses import dataclass
import random

Pairs = Iterator[tuple[Any, Any]]


# class for the color of the node
class Color(enum.Enum):
    """ Class for the color of the node, red or black( 1 or 2 )"""
    RED = enum.auto()  # or just 1
    BLACK = enum.auto()  # or just 2


# class for the leaf
@dataclass
class leaf:
    """Leaf node for the red black tree, color is black by default"""
    color: Color = Color.BLACK


# class for the node
@dataclass
class Node:
    """ Node class for the red black tree, non-leaf node, color is red by default
    
        Attributes:
            value: int  # key or value, is what we are checking for balance, can be int or Any
            # data: Any   # data, what we are storing, can be int or Any
            left: Optional["Node"] = None
            right: Optional["Node"] = None
            parent: Optional["Node"] = None
            color: Color = Color.RED  # default color is red
    """
    value: int  # key or value, is what we are checking for balance, can be int or Any
    # data: Any   # data, what we are storing, can be int or Any
    left: Union["Node", leaf] = leaf()
    right: Union["Node", leaf] = leaf()
    parent: Union["Node", leaf] = leaf()
    color: Color = Color.RED  # default color is red


# Red-Black Tree class
@dataclass
class RBTree:
    # nil as a private attribute
    # root as a public attribute
    _NIL: leaf = leaf()  # leaf node, _NIL is a constant _nil is a variable
    root: Union[Node, leaf] = _NIL

    def search(self, value: int) -> Optional[Node]:
        """ Search for a value in the tree, return the node if found, return None if not found

        Args:
            value (int): value to search for

        Returns:
            Optional[Node]: node if found, None if not found
        """
        return self._search(value=value)

    def _search(self, value: int) -> Optional[Node]:
        """ Search for a value in the tree, return the node if found, return None if not found

        Args:
            value (int):  value to search for

        Returns:
            Optional[Node]: node if found, None if not found
        """

        # if the tree is empty, return None
        current = self.root

        # whil is instance of Node
        while isinstance(current, Node):
            # if value is less than current.value, go left
            if value < current.value:
                current = current.left

            # if value is greater than current.value, go right
            elif value > current.value:
                current = current.right

            # if value is equal to current.value, return current
            else:
                return current

        # if not found, return None
        return None

    def insert(self, value: int) -> None:
        """ Insert a value into the tree

        Args:
            value (int): value to insert into the tree
        """
        # color the new node red
        new_node = Node(value=value, color=Color.RED)
        parent: Union[Node, leaf] = self._NIL
        current: Union[Node, leaf] = self.root

        # while is instance of Node, look for the place to insert the new node
        while isinstance(current, Node):
            parent = current
            # if value is less than current.value, go left
            if value < current.value:
                current = current.left

            # if value is greater than current.value, go right
            elif value > current.value:
                current = current.right

            # if value is equal to current.value, return none
            else:
                return None

        new_node.parent = parent
        # if the parent is a leaf, then the new node is the root
        if isinstance(parent, leaf):
            new_node.color = Color.BLACK
            self.root = new_node

        else:
            # if new_node.value is less than parent.value, insert new_node as the left child of parent
            if new_node.value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node

            # after the insertion, check for the balance, and fix it if needed
            self._insert_fixup(new_node)

    def delete(self, value: int) -> None:
        """ Delete a value from the tree

        Args:
            value (int): value to delete from the tree
        """
        # if the tree is empty, return None
        if (deleting_node := self._search(value=value)) and (isinstance(
                deleting_node, Node)):
            original_color = deleting_node.color

            # case 1: no children or case 2a: one right child
            if isinstance(deleting_node.left, leaf):
                replacing_node = deleting_node.right
                self._transplate(u=deleting_node, v=replacing_node)

                # fix the double black
                if original_color == Color.BLACK:
                    if isinstance(replacing_node, Node):
                        self._delete_fixup(fixing_node=replacing_node)

            # case 2b: only one left child
            elif isinstance(deleting_node.right, leaf):
                replacing_node = deleting_node.left
                self._transplate(u=deleting_node, v=replacing_node)

                # fix the double black
                if original_color == Color.BLACK:
                    if isinstance(replacing_node, Node):
                        self._delete_fixup(fixing_node=replacing_node)

            # case 3: two children
            else:
                replacing_node = self.get_leftmost(deleting_node.right)
                original_color = replacing_node.color
                replacing_replacement = replacing_node.right
                # if the replacing node is the right child of the deleting node
                if replacing_node.parent == deleting_node:
                    if isinstance(replacing_replacement, Node):
                        replacing_replacement.parent = replacing_node
                else:
                    self._transplate(u=replacing_node, v=replacing_replacement)
                    replacing_node.right = deleting_node.right
                    replacing_node.right.parent = replacing_node

                self._transplate(u=deleting_node, v=replacing_node)
                replacing_node.left = deleting_node.left
                replacing_node.left.parent = replacing_node
                replacing_node.color = deleting_node.color
                # fix the double black
                if original_color == Color.BLACK:
                    if isinstance(replacing_replacement, Node):
                        self._delete_fixup(fixing_node=replacing_replacement)

    # -----------------------------------// Auxiliary functions //-----------------------------------#
    @property
    def empty(self) -> bool:
        """ Check if the tree is empty, return True if empty, False if not empty"""
        return (self.root is None) or (self.root is self._NIL)

    @staticmethod
    def get_height(node: Union[leaf, Node]) -> int:
        """ Get the height of a node

        Args:
            node (Union[Node, leaf]): node to get the height of

        Returns:
            int: height of the node. 0 if the subtree has only one node
        """
        # if the node is a leaf, return 0
        if isinstance(node, Node):
            # if the node has two children, return the max height of the two children + 1
            if isinstance(node.left, Node) and isinstance(node.right, Node):
                return (max(RBTree.get_height(node.left),
                            RBTree.get_height(node.right)) + 1)

            # if the node has only one left child, return the height of the left child + 1
            if isinstance(node.left, Node):
                return RBTree.get_height(node=node.left) + 1

            # if the node has only one right child, return the height of the right child + 1
            if isinstance(node.right, Node):
                return RBTree.get_height(node=node.right) + 1

        return 0

    @staticmethod
    def get_leftmost(node: Node) -> Node:
        """ Get the leftmost node of a subtree

        Args:
            node (Node):  root of the subtree

        Returns:
            Node:  leftmost node of the subtree
        """

        current_node = node
        while isinstance(current_node.left, Node):
            current_node = current_node.left
        return current_node

    @staticmethod
    def get_rightmost(node: Node) -> Node:
        """ Get the rightmost node of a subtree

        Args:
            node (Node):  root of the subtree

        Returns:
            Node:  rightmost node of the subtree
        """
        current_node = node
        while isinstance(current_node.right, Node):
            current_node = current_node.right
        return current_node

    @staticmethod
    def get_successor(node: Node) -> Union[Node, leaf]:
        """ Get the successor of a node

        Args:
            node (Node): node to get the successor of

        Returns:
            Union[Node, leaf]: successor of the node
        """

        # case 1: node has a right child
        if isinstance(node.right, Node):
            return RBTree.get_leftmost(node.right)

        # case 2: node has no right child
        parent = node.parent
        while isinstance(parent, Node) and (node == parent.right):
            node = parent
            parent = node.parent
        return parent

    @staticmethod
    def get_predecessor(node: Node) -> Union[Node, leaf]:
        """ Get the predecessor of a node

        Args:
            node (Node): node to get the predecessor of

        Returns:
            Union[Node, leaf]: predecessor of the node
        """
        # case 1: node has a left child
        if isinstance(node.left, Node):
            return RBTree.get_rightmost(node.left)

        # case 2: node has no left child
        parent = node.parent
        while isinstance(parent, Node) and (node == parent.left):
            node = parent
            parent = node.parent
        return node.parent

    def _left_rotate(self, node_x: Node) -> None:
        """ Left rotate the tree

        Args:
            node_x (Node):  node to rotate around

        Returns:
            None
        """
        # set node_y
        node_y = node_x.right
        # node_y cannot be a leaf
        if isinstance(node_y, leaf):
            return None

        # turn node_y's left subtree into node_x's right subtree
        node_x.right = node_y.left
        if isinstance(node_y.left, Node):
            node_y.left.parent = node_x
        node_y.parent = node_x.parent

        # if node parent is a leaf, set node_y as the root
        if isinstance(node_x.parent, leaf):
            self.root = node_y
        # otherwise, set node x parent's left or right child to node_y
        elif node_x == node_x.parent.left:
            node_x.parent.left = node_y
        else:
            node_x.parent.right = node_y

        node_y.left = node_x
        node_x.parent = node_y

    def _right_rotate(self, node_x: Node) -> None:
        """ Right rotate the tree
            
        Args:
            node_x (Node):  node to rotate around
             
        Returns:
            None
        """
        # set node_y
        node_y = node_x.left
        # node_y cannot be a leaf
        if isinstance(node_y, leaf):
            return None
        # turn node_y's right subtree into node_x's left subtree
        node_x.left = node_y.right
        if isinstance(node_y.right, Node):
            node_y.right.parent = node_x
        node_y.parent = node_x.parent

        # if node parent is a leaf, set node_y as the root
        if isinstance(node_x.parent, leaf):
            self.root = node_y
        # otherwise, set node x parent's left or right child to node_y
        elif node_x == node_x.parent.right:
            node_x.parent.right = node_y
        else:
            node_x.parent.left = node_y

        node_y.right = node_x
        node_x.parent = node_y

    def _insert_fixup(self, fixing_node: Node) -> None:
        while fixing_node.parent.color == Color.RED:
            if fixing_node.parent == fixing_node.parent.parent.left:  # type: ignore
                parent_sibling = fixing_node.parent.parent.right  # type: ignore
                if parent_sibling.color == Color.RED:  # Case 1
                    fixing_node.parent.color = Color.BLACK
                    parent_sibling.color = Color.BLACK
                    fixing_node.parent.parent.color = Color.RED  # type: ignore
                    fixing_node = fixing_node.parent.parent  # type: ignore
                else:
                    # Case 2
                    if fixing_node == fixing_node.parent.right:  # type: ignore
                        fixing_node = fixing_node.parent  # type: ignore
                        self._left_rotate(fixing_node)
                    # Case 3
                    fixing_node.parent.color = Color.BLACK
                    fixing_node.parent.parent.color = Color.RED  # type: ignore
                    self._right_rotate(
                        fixing_node.parent.parent)  # type: ignore
            else:
                parent_sibling = fixing_node.parent.parent.left  # type: ignore
                if parent_sibling.color == Color.RED:  # Case 4
                    fixing_node.parent.color = Color.BLACK
                    parent_sibling.color = Color.BLACK
                    fixing_node.parent.parent.color = Color.RED  # type: ignore
                    fixing_node = fixing_node.parent.parent  # type: ignore
                else:
                    # Case 5
                    if fixing_node == fixing_node.parent.left:  # type: ignore
                        fixing_node = fixing_node.parent  # type: ignore
                        self._right_rotate(fixing_node)
                    # Case 6
                    fixing_node.parent.color = Color.BLACK
                    fixing_node.parent.parent.color = Color.RED  # type: ignore
                    self._left_rotate(
                        fixing_node.parent.parent)  # type: ignore

        self.root.color = Color.BLACK

    def _delete_fixup(self, fixing_node: Union[leaf, Node]) -> None:
        while (fixing_node is not self.root) and (fixing_node.color
                                                  == Color.BLACK):
            if fixing_node == fixing_node.parent.left:  # type: ignore
                sibling = fixing_node.parent.right  # type: ignore

                # Case 1: the sibling is red.
                if sibling.color == Color.RED:
                    sibling.color == Color.BLACK
                    fixing_node.parent.color = Color.RED  # type: ignore
                    self._left_rotate(fixing_node.parent)  # type: ignore
                    sibling = fixing_node.parent.right  # type: ignore

                if isinstance(sibling, leaf):
                    break

                # Case 2: the sibling is black and its children are black.
                if (sibling.left.color == Color.BLACK) and (  # type: ignore
                        sibling.right.color == Color.BLACK  # type: ignore
                ):
                    sibling.color = Color.RED
                    # new fixing node
                    fixing_node = fixing_node.parent  # type: ignore

                # Cases 3 and 4: the sibling is black and one of
                # its child is red and the other is black.
                else:
                    # Case 3: the sibling is black and its left child is red.
                    if sibling.right.color == Color.BLACK:  # type: ignore
                        sibling.left.color = Color.BLACK  # type: ignore
                        sibling.color = Color.RED  # type: ignore
                        self._right_rotate(node_x=sibling)  # type: ignore

                    # Case 4: the sibling is black and its right child is red.
                    sibling.color = fixing_node.parent.color  # type: ignore
                    fixing_node.parent.color = Color.BLACK  # type: ignore
                    sibling.right.color = Color.BLACK  # type: ignore
                    self._left_rotate(
                        node_x=fixing_node.parent)  # type: ignore
                    # Once we are here, all the violation has been fixed, so
                    # move to the root to terminate the loop.
                    fixing_node = self.root
            else:
                sibling = fixing_node.parent.left  # type: ignore

                # Case 5: the sibling is red.
                if sibling.color == Color.RED:
                    sibling.color == Color.BLACK  # type: ignore
                    fixing_node.parent.color = Color.RED  # type: ignore
                    self._right_rotate(
                        node_x=fixing_node.parent)  # type: ignore
                    sibling = fixing_node.parent.left  # type: ignore

                if isinstance(sibling, leaf):
                    break

                # Case 6: the sibling is black and its children are black.
                if (sibling.right.color == Color.BLACK) and (  # type: ignore
                        sibling.left.color == Color.BLACK  # type: ignore
                ):
                    sibling.color = Color.RED
                    fixing_node = fixing_node.parent  # type: ignore
                else:
                    # Case 7: the sibling is black and its right child is red.
                    if sibling.left.color == Color.BLACK:  # type: ignore
                        sibling.right.color = Color.BLACK  # type: ignore
                        sibling.color = Color.RED
                        self._left_rotate(node_x=sibling)  # type: ignore
                    # Case 8: the sibling is black and its left child is red.
                    sibling.color = fixing_node.parent.color  # type: ignore
                    fixing_node.parent.color = Color.BLACK  # type: ignore
                    sibling.left.color = Color.BLACK  # type: ignore
                    self._right_rotate(
                        node_x=fixing_node.parent)  # type: ignore
                    # Once we are here, all the violation has been fixed, so
                    # move to the root to terminate the loop.
                    fixing_node = self.root

        fixing_node.color = Color.BLACK

    def _transplate(self, u: Node, v: Union[Node, leaf]) -> None:
        """Transplate u for v.

        Args:
            u (Node): The node to transplate.
            v (Node): The node to transplate for.
        """
        if isinstance(u.parent, leaf):
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if isinstance(v, Node):
            v.parent = u.parent

    def fill_tree_random(self, size: int, max_value: int) -> None:
        """Fill the tree with random values.

        Args:
            size (int): The size of the tree.
            max_value (int): The maximum value of the tree.
        """
        for _ in range(size):
            self.insert(random.randint(0, max_value))

    def fill_tree_order(self, size: int) -> None:
        """Fill the tree with ordered values.

        Args:
            size (int): The size of the tree.
        """
        for i in range(size):
            self.insert(i)

    def clear(self) -> None:
        """Clear the tree."""
        self.root = leaf()

    # -----------------------------------// Traversal //-----------------------------------#

    def inorder_transverse(self) -> Iterable:
        """ Inorder transverse of the tree

        Yields:
            Pairs: (key, value) pairs
        """
        return self._inorder_traverse(node=self.root)
        #yield from self._inorder_traverse(self.root)

    def preorder_transverse(self) -> Iterable:
        """ Preorder transverse of the tree

        Yields:
            Pairs: (key, value) pairs
        """
        # yield from self._preorder_traverse(self.root)
        return self._preorder_traverse(node=self.root)

    def postorder_transverse(self) -> Iterable:
        """ Postorder transverse of the tree

        Yields:
            Pairs: (key, value) pairs
        """
        #yield from self._postorder_traverse(self.root)
        return self._postorder_traverse(node=self.root)

    def _inorder_traverse(self, node: Union[Node, leaf]) -> Iterable:
        if isinstance(node, Node):
            yield from self._inorder_traverse(node.left)
            yield (node.value)
            yield from self._inorder_traverse(node.right)

    def _preorder_traverse(self, node: Union[Node, leaf]) -> Iterable:
        if isinstance(node, Node):
            yield (node.value)
            yield from self._preorder_traverse(node.left)
            yield from self._preorder_traverse(node.right)

    #  # or pairs ?
    def _postorder_traverse(self, node: Union[Node, leaf]) -> Iterable:
        if isinstance(node, Node):
            yield from self._postorder_traverse(node.left)
            yield from self._postorder_traverse(node.right)
            yield (node.value)

    # -----------------------------------// Print //-----------------------------------#

    def print_tree_inorder(self) -> None:
        """Print the tree in order."""
        print("Inorder transverse:")
        for pair in self.inorder_transverse():
            print(f"{pair}", end=" ")

    def print_tree_preorder(self) -> None:
        """Print the tree in preorder."""
        print("Preorder transverse:")
        for pair in self.preorder_transverse():
            print(f"{pair}", end=" ")

    def print_tree_postorder(self) -> None:
        """Print the tree in postorder."""
        print("Postorder transverse:")
        for pair in self.postorder_transverse():
            print(f"{pair}", end=" ")

    def print_tree(self) -> None:
        """Print the tree."""
        print("\nTree:\n")
        self._print_tree(self.root, 0)

    def _print_tree(self, node: Union[Node, leaf], level: int) -> None:
        if isinstance(node, Node):
            self._print_tree(node.right, level + 1)
            print(" " * 4 * level, node.value)
            self._print_tree(node.left, level + 1)

    def print_tree_color(self) -> None:
        """Print the tree with colors."""
        print("\nTree:\n")
        self._print_tree_color(self.root, 0)

    def _print_tree_color(self, node: Union[Node, leaf], level: int) -> None:
        if isinstance(node, Node):
            self._print_tree_color(node.right, level + 1)
            print(" " * 4 * level, node.value, node.color)
            self._print_tree_color(node.left, level + 1)

    def print_level_order(self) -> None:
        """Print the tree in level order."""
        height = self.get_height(self.root)
        print(f"Height of the tree: {height}")
        # the height of the tree is the number of levels
        for i in range(1, height + 2):
            print(f"Level {i}: ", end="")
            self._print_given_level(self.root, i)
            print()

    def _print_given_level(self, node: Union[Node, leaf], level: int) -> None:
        if isinstance(node, Node):
            if level == 1:
                print(node.value, end=" ")
            elif level > 1:
                self._print_given_level(node.left, level - 1)
                self._print_given_level(node.right, level - 1)


# -----------------------------------// Test //-----------------------------------#

# create a tree
tree = RBTree()

lst = [
    39, 27, 12, 10, 8, 9, 30, 54, 88, 5, 19, 25, 34, 44, 61, 79, 97, 1, 11, 21,
    28, 31, 38, 40, 50, 57, 67, 94, 98, 33, 47, 55
]

# fill the tree with lst
for i in lst:
    tree.insert(i)

# print the tree in order
tree.print_tree_inorder()

# delete a node
tree.delete(39)

# print the tree in order
tree.print_tree_inorder()

# print the tree in preorder
tree.print_tree_preorder()

# print the tree in postorder
tree.print_tree_postorder()

# print the tree
tree.print_tree()

# print the tree with colors
tree.print_tree_color()

# print the tree in level order
tree.print_level_order()

# clear the tree
tree.clear()
