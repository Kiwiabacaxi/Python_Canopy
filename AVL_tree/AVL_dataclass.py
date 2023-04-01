from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    key: Any
    data: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    height: int = 0                 # in case of an AVL tree


"""
# dataclass is a decorator that automatically generates the __init__ method
class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 0 """


class AVLTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    # -> str is a type hint accessible at runtime with __annotations__
    def __repr__(self) -> str:
        if self.root is None:
            return (f"{type(self)}, root={self.root}, "
                    f"tree_height={str(self.get_height(self.root))}")
        return f"empty tree"

    def search(self, key: Any) -> Optional[Node]:
        return None

    def insert(self, key: Any, data: Any) -> None:
        

    def delete(self, key: Any) -> None:
        pass

    @staticmethod
    def get_leftmost(node: Node) -> Node:

    @staticmethod
    def get_rightmost(node: Node) -> Node:

    @staticmethod
    def get_successor(node: Node) -> Optional[Node]:

    @staticmethod
    def get_predecessor(node: Node) -> Optional[Node]:

    @staticmethod
    def get_height(node: Optional[Node]) -> int:

    def _get_balance_factor(self, node: Optional[Node]) -> int:

    def _left_rotate(self, node_x: Node) -> None:

    def _right_rotate(self, node_x: Node) -> None:

    def _insert_fixup(self, new_node: Node) -> None:

    def _transplant(self, deleting_node: Node, replacing_node: Optional[Node]) -> None:

    def _delete_no_child(self, deleting_node: Node) -> None:

    def _delete_one_child(self, deleting_node: Node) -> None:

    def _delete_fixup(self, fixing_node: Node) -> None:






print(Node.__annotations__)
print(AVLTree.__annotations__)
