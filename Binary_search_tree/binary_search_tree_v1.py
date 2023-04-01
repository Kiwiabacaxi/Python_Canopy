from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class Node:
    key: Any  # key to be used for sorting, the "key/value"
    data: Any  # data associated with key, the "true value/cargo"
    left: Optional["Node"] = None  # pointer to left child
    right: Optional["Node"] = None  # pointer to right child
    parent: Optional["Node"] = None  # pointer to parent node


class DuplicateKeyError(Exception):
    # str instead of Any because we're only using strings
    def __init__(self, key: str) -> None:
        Exception.__init__(self, f"{key} already exists.")


class BinarySearchTree:

    def __init__(self) -> None:
        # root node of the tree
        self.root: Optional[Node] = None

    def __repr__(self) -> str:
        if self.root:
            return (
                f"{type(self)}, root={self.root}, "
                f"tree_height={str(self.get_height(self.root))}"
            )
        return "empty tree"

    def search(self, key: Any) -> Optional[Node]:
        # partindo da raiz
        current = self.root

        while current is not None:
            # caso 1 - chave é igual ao nó atual
            if key == current.key:
                return current
            # caso 2 - chave é maior que o nó atual
            elif key < current.key:
                current = current.left
            # caso 3 - chave é menor que o nó atual
            else:
                current = current.right

        return None

    def insert(self, key: Any, data: Any) -> None:
        # parent and current types
        parent: Optional[Node] = None
        current: Optional[Node] = self.root
        # initialize current node to root
        new_node = Node(key=key, data=None)

        # loop until current is None
        while current is not None:  # or while current:
            parent = current
            # se a chave for menor vai para a esquerda
            if new_node.key < current.key:
                current = current.left
            # se a chave for maior vai para a direita
            elif new_node.key > current.key:
                current = current.right
            # se a chave for igual retorna o nó
            else:
                raise DuplicateKeyError(key)

        # no novo nó o pai recebe o pai do nó atual
        new_node.parent = parent

        # se a arvore estiver vazia o novo nó é a raiz
        if parent is None:
            self.root = new_node  # raiz recebe o novo nó
        elif new_node.key < parent.key:
            parent.left = new_node  # se a chave for menor que o pai, o novo nó é o filho da esquerda
        else:
            parent.right = new_node  # se a chave for maior que o pai, o novo nó é o filho da direita

    def delete(self, key: Any) -> None:
        """ Delete a node according to the key.
        
        
        The binary search tree's deletion has three cases –
        1 - the node to be deleted has no child,
        2 - one child,
        3 - or two children.
        """
        """"
        # verifica se duas condições são verdadeiras
        # a primeira é se a raiz existe
        # a segunda é uma atribuição walrus
        # deleting_node := self.search(key=key)" é uma expressão de atribuição
        que procura por um nó na árvore de busca binária com uma chave fornecida.
        Se um nó com a chave fornecida for encontrado, sua referência é atribuída à variável "deleting_node".
        Assim, se ambas as condições forem verdadeiras,
        significa que a árvore de busca binária possui um nó raiz e um nó com a chave fornecida existe na árvore.
        """

        #if self.root and (deleting_node := self.search(key=key)):
        if self.root is not None and (deleting_node := self.search(key=key)):

            # caso 1: sem filhos ou um filho a direita
            if deleting_node.left is None:
                self._transplant(
                    deleting_node=deleting_node,
                    replacing_node=deleting_node.right
                )  # substitui o nó a ser deletado pelo filho a direita

            # caso 2: um filho a esquerda
            elif deleting_node.left is not None:
                self._transplant(
                    deleting_node=deleting_node,
                    replacing_node=deleting_node.left
                )  # substitui o nó a ser deletado pelo filho a esquerda

            # caso 3: dois filhos
            else:
                replacing_node = BinarySearchTree.get_leftmost(
                    node=deleting_node.right
                )  # o nó a ser subistituido é o nó mais a esquerda do filho a direita

                # caso 3.1: o nó mais a esquerda não é filho direito do nó a ser deletado
                if replacing_node.parent is not deleting_node:
                    self._transplant(
                        deleting_node=replacing_node,
                        replacing_node=replacing_node.right
                    )  # substitui o nó a ser deletado pelo filho a direita

                    replacing_node.right = deleting_node.right  # o filho a direita do nó a ser deletado é o filho a direita do nó a ser substituido
                    replacing_node.right.parent = replacing_node  # o pai do filho a direita do nó a ser deletado é o nó a ser substituido

                self._transplant(
                    deleting_node=deleting_node, replacing_node=replacing_node
                )  # substitui o nó a ser deletado pelo nó a ser substituido
                
                replacing_node.left = deleting_node.left  # o filho a esquerda do nó a ser deletado é o filho a esquerda do nó a ser substituido
                replacing_node.left.parent = replacing_node  # o pai do filho a esquerda do nó a ser deletado é o nó a ser substituido
                

    # Aux functions - transplant, get_leftmost, get_rightmost, get_successor, get_predecessor
    @staticmethod
    def get_leftmost(node: Node) -> Node:
        """Return the leftmost node from a given subtree.
        The key of the leftmost node is the smallest key in the given subtree.
        Parameters
        ----------
        node: `Node`
            The root of the subtree.
        Returns
        -------
        `Node`
            The node whose key is the smallest from the subtree of
            the given node.
        """
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    @staticmethod
    def get_rightmost(node: Node) -> Node:
        """Return the rightmost node from a given subtree.
        The key of the rightmost node is the biggest key in the given subtree.
        Parameters
        ----------
        node: `Node`
            The root of the subtree.
        Returns
        -------
        `Node`
            The node whose key is the biggest from the subtree of
            the given node.
        """
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    @staticmethod
    def get_successor(node: Node) -> Optional[Node]:
        """Return the successor in the in-order order.
        Parameters
        ----------
        node: `Node`
            The node to get its successor.
        Returns
        -------
        `Optional[Node]`
            The successor node.
        """
        if node.right:  # Case 1: right child is not empty
            return BinarySearchTree.get_leftmost(node=node.right)
        # Case 2: right child is empty
        parent = node.parent
        while parent and (node == parent.right):
            node = parent
            parent = parent.parent
        return parent

    @staticmethod
    def get_predecessor(node: Node) -> Optional[Node]:
        """Return the predecessor in the in-order order.
        Parameters
        ----------
        node: `Node`
            The node to get its predecessor.
        Returns
        -------
        `Optional[Node]`
            The predecessor node.
        """
        if node.left:  # Case 1: left child is not empty
            return BinarySearchTree.get_rightmost(node=node.left)
        # Case 2: left child is empty
        parent = node.parent
        while parent and (node == parent.left):
            node = parent
            parent = parent.parent
        return parent

    @staticmethod
    def get_height(node: Node) -> int:
        """Get the height of the given subtree.
        Parameters
        ----------
        node: `Node`
            The root of the subtree to get its height.
        Returns
        -------
        `int`
            The height of the given subtree. 0 if the subtree has only one node.
        """
        if node.left and node.right:
            return (
                max(
                    BinarySearchTree.get_height(node=node.left),
                    BinarySearchTree.get_height(node=node.right),
                )
                + 1
            )

        if node.left:
            return BinarySearchTree.get_height(node=node.left) + 1

        if node.right:
            return BinarySearchTree.get_height(node=node.right) + 1

        # If reach here, it means the node is a leaf node.
        return 0
    
    def _transplant(self, deleting_node: Node,
                    replacing_node: Optional[Node]) -> None:
        """
        Internal function to transplant a subtree rooted at node deleting_node with a subtree rooted at node replacing_node.


        The transplant method replaces the subtree rooted at node
        deleting_node with the subtree rooted at node replacing_node.
        After the replacing_node replaces the deleting_node, the parent of the
        deleting_node becomes the replacing_node's parent,
        and the deleting_node's parent ends up having the replacing_node as its child.
        Since the function is internal, we define the function with a leading underscore, i.e., _transplant.
        credit: shunsvineyard.info and Introduction to Algorithms

        """
        #
        if deleting_node.parent is None:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node

        if replacing_node:
            replacing_node.parent = deleting_node.parent

# Testes
tree = BinarySearchTree()

print(type(tree))

# for with a list
for i in range(10):
    tree.insert(key=i, data=i)
    
print(tree)
# printing the tree
while tree.root:
    print(f"key: {tree.root.key}, data: {tree.root.data}")
    tree.delete(key=tree.root.key)
    
    

print(repr(BinarySearchTree()))