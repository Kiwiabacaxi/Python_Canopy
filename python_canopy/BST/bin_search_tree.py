from typing import List, Optional, Any
from dataclasses import dataclass
import random


@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None  # parent node, pointer to parent node


@dataclass
class BinarySearchTree:
    root: Optional[Node] = None

    def insert(self, value: int) -> None:
        """Inserts a value into the tree.

        Args:
            value (int): The value to insert.
        """
        # if the tree is empty, create a node with the value
        if self.root is None:
            self.root = Node(value)

        # otherwise, call the private method
        else:
            self._insert(value, self.root)

    def _insert(self, value: int, current: Node) -> None:
        """Private method to insert a value into the tree.

        Args:
            value (int): The value to insert.
            current (Optional[Node]): The current node to compare the value to.
        """
        # case 1: if the value is less than the current node's value
        if value < current.value:
            # if the left child is None, create a node with the value
            if current.left is None:
                current.left = Node(
                    value, parent=current
                )  # or current.left = Node(value) and current.left.parent = current
            # otherwise, call the private method
            else:
                self._insert(value, current.left)

        # case 2: if the value is greater than the current node's value
        elif value > current.value:
            # if the right child is None, create a node with the value
            if current.right is None:
                current.right = Node(value, parent=current)
            # otherwise, call the private method
            else:
                self._insert(value, current.right)

        # case 3: if the value is equal to the current node's value, do nothing
        else:
            pass

    def print_tree(self) -> None:
        """Prints the tree in order."""
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current: Optional[Node]) -> None:
        """Private method to print the tree in order.

        Args:
            current (Optional[Node]): The current node to print.
        """
        if current is not None:
            # print in order
            self._print_tree(current.left)
            print(str(current.value))
            self._print_tree(current.right)

    def search(self, value: int) -> bool:
        """Searches for a value in the tree.

        Args:
            value (int): The value to search for.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        # if the tree is empty, return False
        if self.root is None:
            return False

        # otherwise, call the private method
        else:
            return self._search(value, self.root)

    def _search(self, value: int, current: Optional[Node]) -> bool:
        """Private method to search for a value in the tree.

        Args:
            value (int): The value to search for.
            current (Optional[Node]): The current node to compare the value to.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        # case 1: if the current node is None, return False
        if current is None:
            return False

        # case 2: if the value is less than the current node's value, search the left subtree
        elif value < current.value:
            return self._search(value, current.left)

        # case 3: if the value is greater than the current node's value, search the right subtree
        elif value > current.value:
            return self._search(value, current.right)

        # case 4: if the value is equal to the current node's value, return True
        else:
            return True

    def search_path(self, value: int) -> List[int]:
        """Searches for a value in the tree and returns the path to the value.

        Args:
            value (int): The value to search for.

        Returns:
            List[int]: The path to the value.
        """
        # if the tree is empty, return an empty list
        if self.root is None:
            return []  # empty list, vai dar problema se for None?

        # otherwise, call the private method
        else:
            return self._search_path(value, self.root, [])

    def _search_path(self, value: int, current: Optional[Node],
                     path: List[int]) -> List[int]:
        """Private method to search for a value in the tree and return the path to the value.

        Args:
            value (int): The value to search for.
            current (Optional[Node]): The current node to compare the value to.
            path (List[int]): The path to the current node, the list beggins empty.

        Returns:
            List[int]: The path to the value.
        """
        # case 1: if the current node is None, return an empty list
        if current is None:
            return []

        # case 2: if the value is less than the current node's value, search the left subtree
        elif value < current.value:
            path.append(current.value)
            return self._search_path(value, current.left, path)

        # case 3: if the value is greater than the current node's value, search the right subtree
        elif value > current.value:
            path.append(current.value)
            return self._search_path(value, current.right, path)

        # case 4: if the value is equal to the current node's value, return the path
        else:
            path.append(current.value)
            return path

    def search_node(self, value: int) -> Optional[Node]:
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
            return self._search_node(value=value)

    def _search_node(self, value: int) -> Optional[Node]:
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

    # Delete function using the transplate method and the search_node method
    def delete(self, value: int) -> None:
        """Deletes a node from the tree.

        Args:
            value (int): The value to delete.
        """
        # if the tree is empty, return None
        if self.root and (deleting_node := self._search_node(value=value)):

            # case 1: no child or case 2: one right child
            if deleting_node.left is None:
                self._transplate(u=deleting_node, v=deleting_node.right)

            # case 2b: one left left child
            elif deleting_node.right is None:
                self._transplate(u=deleting_node, v=deleting_node.left)

            # case 3: two children
            else:
                # get the leftmost node of the right subtree
                replacing_node = self.get_leftmost_node(node=deleting_node.right) # self or BinarySearchTree?
                # the leftmost node is not the direct child of the node to be deleted
                if replacing_node.parent != deleting_node:
                    # transplate the leftmost node for its right child
                    self._transplate(u=replacing_node, v=replacing_node.right)
                    # set the right child of the node to be deleted as the right child of the leftmost node
                    replacing_node.right = deleting_node.right
                    # set the parent of the right child of the node to be deleted as the leftmost node
                    replacing_node.right.parent = replacing_node
                    
                # transplate the node to be deleted for the leftmost node
                self._transplate(u=deleting_node, v=replacing_node)
                replacing_node.left = deleting_node.left
                replacing_node.left.parent = replacing_node
                

    # Aux function

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

    @staticmethod # staticmethod() é uma função que não precisa de self
    def get_leftmost_node(node: Node) -> Node:
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
    def get_rightmost_node(node: Node) -> Node:
        """Gets the rightmost node of a subtree.

        Args:
            node (Node): The root of the subtree.

        Returns:
            Node: The rightmost node of the subtree.
        """
        while node.right is not None:
            node = node.right
        return node

    def height(self) -> int:
        """Calculates the height of the tree.

        Returns:
            int: The height of the tree.
        """
        # if the tree is empty, return 0
        if self.root is None:
            return 0
        # otherwise, call the private method
        else:
            return self._height(self.root, 0)

    def _height(self, current: Optional[Node], current_height: int) -> int:
        """Private method to calculate the height of the tree.

        Args:
            current Optional[Node]: The current node to calculate the height from.
            current_height (int): The current height.

        Returns:
            int: The height of the tree.
        """
        # if the current node is None, return the current height
        if current is None:
            return current_height

        # otherwise, calculate the height of the left and right subtrees
        left_height = self._height(current.left, current_height + 1)
        right_height = self._height(current.right, current_height + 1)

        # return the maximum height
        return max(left_height, right_height)

    def fill_tree_random(self, num_elements: int, max_int: int) -> Any:
        """Fills the tree with random values.

        Args:
            num_elements (int): The number of elements to insert.
            max_int (int): The maximum integer value to insert.
        """
        for _ in range(num_elements):
            current = random.randint(0, max_int)
            self.insert(current)
        return self

    def fill_tree_ordered(self, num_elements: int) -> Any:
        """Fills the tree with ordered values.

        Args:
            num_elements (int): The number of elements to insert.
        """
        for i in range(num_elements):
            self.insert(i + 1)
        return self

    def find(self, value: int) -> Optional[Node]:
        """Finds a value in the tree.

        Args:
            value (int): The value to find.

        Returns:
            Optional[Node]: The node containing the value.
        """
        # if the tree is empty, return None
        if self.root is None:
            return None

        # otherwise, call the private method
        else:
            return self._find(value, self.root)

    def _find(self, value: int, current: Optional[Node]) -> Optional[Node]:
        """Private method to find a value in the tree.

        Args:
            value (int): The value to find.
            current (Optional[Node]): The current node to compare the value to.

        Returns:
            Optional[Node]: The node containing the value.
        """
        # case 1: if the current node is None, return None
        if current is None:
            return None

        # case 2: if the value is less than the current node's value, search the left subtree
        elif value < current.value:
            return self._find(value, current.left)

        # case 3: if the value is greater than the current node's value, search the right subtree
        elif value > current.value:
            return self._find(value, current.right)

        # case 4: if the value is equal to the current node's value, return the node
        else:
            return current


""" # testing the code
tree = BinarySearchTree()

#tree = BinarySearchTree.fill_tree_ordered(tree, 20)
tree = BinarySearchTree.fill_tree_random(tree, 20, 100)

print(f"Height of the tree: {tree.height()}")

tree.print_tree()

# searching for a value
a = 10 
#int(input("Enter a value to search for: "))
print(tree.search(a))

# searching for a value and returning the path
b = 15 
#int(input("Enter a value to search for: "))
print(tree.search_path(b))

# test get_leftmost_node
leftmost_node = tree.get_leftmost_node(tree.root)
rightmost_node = tree.get_rightmost_node(tree.root)
print(f"Leftmost node: {leftmost_node.value}")
print(f"Rightmost node: {rightmost_node.value}")

# test delete
tree.delete(int(input("Enter a value to delete: ")))

print(f"Height of the tree: {tree.height()}")
print(f"Leftmost node: {leftmost_node.value}")
print(f"Rightmost node: {rightmost_node.value}")
tree.print_tree()

tree2 = BinarySearchTree()

tree2.insert(5)
tree2.insert(4)
tree2.insert(6)
tree2.insert(10)
tree2.insert(9)
tree2.insert(11)

tree2.print_tree()
print(f"Height of the tree: {tree2.height()}")
print()

tree2.delete(5)
tree2.delete(4)
tree2.delete(11)

tree2.print_tree()
print(f"Height of the tree: {tree2.height()}") """