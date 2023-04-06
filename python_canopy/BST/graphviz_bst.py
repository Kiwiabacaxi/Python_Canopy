# importing graphviz
import graphviz

# importing BST
from bin_search_tree import BinarySearchTree

# using graphviz to visualize BST

# creating a BST
tree = BinarySearchTree()

# tree.fill_tree_ordered(num_elements=20)
tree.fill_tree_random(num_elements=20, max_int=100)

# inserting values into BST
# while value is not equal to -1
""" while True:

    # getting value from user
    value = int(input("Enter value to insert into BST: "))
    # if value is equal to -1
    
    if value == -1:
        break
    # insert value into BST
    else:
        tree.insert(value) """
        
# creating a graph
graph = graphviz.Digraph()

# creating a function to visualize BST
def visualize_bst(tree, graph):
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

# unflattening the graph
# graph.graph_attr['rankdir'] = 'BT' # BT = bottom to top
# graph.graph_attr['rankdir'] = 'LR' # LR = left to right
# graph.graph_attr['rankdir'] = 'RL' # RL = right to left
# graph.graph_attr['rankdir'] = 'TB' # TB = top to bottom
# graph.graph_attr['rankdir'] = 'TD' # TD = top down
# graph.graph_attr['rankdir'] = 'DU' # DU = down up
# graph.graph_attr['rankdir'] = 'UD' # UD = up down
graph.unflatten(stagger=50)

# calling visualize_bst
visualize_bst(tree.root, graph)

tree.print_level_order()

# saving graph to file, rendering it as a png and saving it as bst_graph on the same folder
graph.render(engine='dot', format='png', filename='bst_graph',directory="python_canopy\BST\\bst_graph")

