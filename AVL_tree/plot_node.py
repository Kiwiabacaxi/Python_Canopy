import matplotlib.pyplot as plt

# Define a recursive function to traverse the tree and plot each node
def plot_node(ax, node, x, y, level, parent_x=None, parent_y=None):
    if node is None:
        return

    # Compute the x and y coordinates of the node
    if parent_x is not None and parent_y is not None:
        if node == node.parent.left:
            x = parent_x - 2**(max_level - level + 1)
        else:
            x = parent_x + 2**(max_level - level + 1)
    ax.plot(x, y, 'o', markersize=30, fillstyle='none', lw=2)
    ax.text(x, y, str(node.key), ha='center', va='center', fontsize=20)

    # Recursively plot the left and right subtrees
    plot_node(ax, node.left, x - 2**(max_level - level), y - 50, level + 1, x, y)
    plot_node(ax, node.right, x + 2**(max_level - level), y - 50, level + 1, x, y)

# Create an example AVL tree
# assume we have an AVL tree with root node "root"
root = Node(10)
root = root.insert(5)
root = root.insert(20)
root = root.insert(15)
root = root.insert(25)
root = root.insert(23)
root = root.insert(26)

# Compute the maximum depth of the tree
max_level = root.get_depth()

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.axis('off')
ax.set_xlim(-2**(max_level+1), 2**(max_level+1))
ax.set_ylim(-100, -100*(max_level+1))

# Plot the tree
plot_node(ax, root, 0, 0, 1)

# Show the plot
plt.show()