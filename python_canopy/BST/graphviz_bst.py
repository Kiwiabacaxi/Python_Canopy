import graphviz
from bin_search_tree import Node, BinarySearchTree
from typing import Optional


def visualize_bst(tree: Optional[Node], graph: graphviz.Digraph):
    """Visualize a binary search tree using graphviz.

    Args:
        tree (BinarySearchTree): The binary search tree to visualize.
        graph (Digraph): The graphviz graph to add the tree to.
    """

    # customize the graph
    graph.engine = "dot"

    graph.attr("node",
               shape="circle",
               fontcolor="black",
               fontname="Arial",
               fontsize="12",
               width="0.5",
               height="0.5")

    # if tree is not empty
    if tree is not None:
        # if left child is not empty
        if tree.left is not None:
            # add edge from parent to left child
            graph.edge(str(tree.value), str(tree.left.value))
        # if right child is not empty
        if tree.right is not None:
            # add edge from parent to right child
            graph.edge(str(tree.value), str(tree.right.value))
        # recursively call visualize_bst on left child
        visualize_bst(tree.left, graph)
        # recursively call visualize_bst on right child
        visualize_bst(tree.right, graph)


# find the given value and change its color to green
def find_node(tree: Optional[Node], graph: graphviz.Digraph, value: int):
    """Find a node in a binary search tree and change its color to green.

    Args:
        tree (BinarySearchTree): The binary search tree to find the node in.
        graph (Digraph): The graphviz graph to add the tree to.
        value (int): The value of the node to find.
    """

    # customize the graph
    graph.engine = "dot"

    graph.attr("node",
               shape="circle",
               fontcolor="black",
               fontname="Arial",
               fontsize="12",
               width="0.5",
               height="0.5")

    # if tree is not empty
    if tree is not None:
        # if the value is found
        if tree.value == value:
            # change the color of the node to green
            graph.node(str(tree.value), color="green", style="filled")
        # recursively call find_node on left child
        find_node(tree.left, graph, value)
        # recursively call find_node on right child
        find_node(tree.right, graph, value)
