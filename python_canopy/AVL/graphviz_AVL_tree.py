from typing import Optional
from AVL_tree import AVLTree, Node
import graphviz


class AVLTreeGraph(AVLTree):  #
    """ AVL Tree Graph Class """

    def __init__(self):
        """ Initialize the AVL Tree Graph """
        super().__init__()

    def visualize_avl(self, tree: Optional[Node], graph: graphviz.Digraph):
        """ Visualize an AVL tree using graphviz.

        Args:
            tree (AVLTree): The AVL tree to visualize.
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
            # recursively call visualize_avl on left child
            self.visualize_avl(tree.left, graph)
            # recursively call visualize_avl on right child
            self.visualize_avl(tree.right, graph)

    def find_node(self, tree: Optional[Node], graph: graphviz.Digraph,
                  value: int):
        """ Find a node in an AVL tree and change its color to green.

        Args:
            tree (AVLTree): The AVL tree to find the node in.
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
            self.find_node(tree.left, graph, value)
            # recursively call find_node on right child
            self.find_node(tree.right, graph, value)


# create a tree
avl = AVLTreeGraph()

# list
lst = [
    59, 16, 9, 8, 0, 6, 15, 41, 27, 23, 19, 17, 21, 40, 39, 32, 38, 53, 49, 47,
    46, 43, 48, 50, 55, 95, 72, 69, 64, 61, 65, 71, 89, 76, 73, 74, 85, 93, 96,
    100
]

# insert nodes
for i in lst:
    avl.insert(i)

# create a graph
graph = graphviz.Digraph()

# visualize the tree
avl.visualize_avl(avl.root, graph)

# find a node
avl.find_node(avl.root, graph, 59)

# save the graph
graph.render(directory='python_canopy/AVL/avl_graph',
             filename='avl_tree_graph',
             format='png')
