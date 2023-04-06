from typing import List, Optional, Any
from dataclasses import dataclass
import random


@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


@dataclass
class BinarySearchTree:
    root: Optional[Node] = None

    def insert(self, value: int) -> None:
        """Inserts a value into the tree.

        Args:
            value (int): The value to insert.
        
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: int, current: Node) -> None:
        """Private method to recursively insert a value into the tree.

        Args:
            value (int): The value to insert.
            current (Node): The current node to compare the value to.
        """
        # case 1: if the value is less than the current node's value, go left
        if value < current.value:

            # if there is no left child, create a node with the value
            if current.left is None:
                current.left = Node(value)

            # if there is a left child, call the _insert method recursively
            else:
                self._insert(value, current.left)

        # case 2: if the value is greater than the current node's value, go right
        elif value > current.value:

            # if there is no right child, create a node with the value
            if current.right is None:
                current.right = Node(value)

            # if there is a right child, call the _insert method recursively
            else:
                self._insert(value, current.right)

        # case 3: if the value is equal to the current node's value, do nothing
        else:
            print("Skipping duplicate value")

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
            return [] # empty list, vai dar problema se for None?

        # otherwise, call the private method
        else:
            return self._search_path(value, self.root, [])
        
    def _search_path(self, value: int, current: Optional[Node], path: List[int]) -> List[int]:
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
        
        
    # Aux function

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


# testing the code
tree = BinarySearchTree()

tree = BinarySearchTree.fill_tree_ordered(tree, 20)

print(f"Height of the tree: {tree.height()}")

tree.print_tree()

# searching for a value
a = int(input("Enter a value to search for: "))
print(tree.search(a))

# searching for a value and returning the path
b = int(input("Enter a value to search for: "))
print(tree.search_path(b))
