from typing import Any, Optional, Union, Iterable
from RBTree import *
import graphviz


class RBTreeGraphviz(RBTree):
    """Red-black tree graphviz class.
    
    Attributes:
        root (Node): The root node of the tree.
        
    Methods:
        visualize() -> None: Visualize the tree using Graphviz.
        _add_nodes(node: Union[Node, leaf], dot: graphviz.Digraph) -> None: Add nodes to the graph.
        _add_edges(node: Union[Node, leaf], dot: graphviz.Digraph) -> None: Add edges to the graph.
    """

    def __init__(self) -> None:
        """Initialize the red-black tree graphviz class."""
        super().__init__()

    def visualize(self) -> None:
        """Visualize the tree using Graphviz."""
        dot = graphviz.Digraph()

        # customize the graph
        dot.engine = "dot"
        dot.attr("node",
                 shape="circle",
                 fontcolor="white",
                 fontname="Arial",
                 fontsize="12",
                 width="0.5",
                 height="0.5")

        # add nodes to the graph
        self._add_nodes(self.root, dot)

        # add edges to the graph
        self._add_edges(self.root, dot)

        # render and view the graph, format to png
        #dot.render("red_black_tree.gv", view=True, format="png")

    def _add_nodes(self, node: Union[Node, leaf],
                   dot: graphviz.Digraph) -> None:
        if isinstance(node, Node):
            color = "red" if node.color == Color.RED else "black"
            dot.node(str(node.value),
                     str(node.value),
                     fillcolor=color,
                     style="filled")
            self._add_nodes(node.left, dot)
            self._add_nodes(node.right, dot)

    def _add_edges(self, node: Union[Node, leaf],
                   dot: graphviz.Digraph) -> None:
        if isinstance(node, Node):
            if node.left is not None and not isinstance(node.left, leaf):
                dot.edge(str(node.value), str(node.left.value), color="black")
            if node.right is not None and not isinstance(node.right, leaf):
                dot.edge(str(node.value), str(node.right.value), color="black")
            self._add_edges(node.left, dot)
            self._add_edges(node.right, dot)
