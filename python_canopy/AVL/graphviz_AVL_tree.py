from typing import Optional
from AVL_tree import AVLTree, Node
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


# create a tree
avl = AVLTreeGraph()

# list
lst = [
    59, 16, 9, 8, 0, 6, 15, 41, 27, 23, 19, 17, 21, 40, 39, 32, 38, 53, 49, 47,
    46, 43, 48, 50, 55, 95, 72, 69, 64, 61, 65, 71, 89, 76, 73, 74, 85, 93, 96
]

# insert nodes
for i in lst:
    avl.insert(i)

# graph the tree
avl.graphviz()

# save the graph
avl.graphviz().render(directory='python_canopy/AVL/avl_graph',filename='avl_tree_graph', format='png')