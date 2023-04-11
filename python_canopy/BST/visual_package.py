import graphviz
from bin_search_tree import BinarySearchTree, Node
from graphviz_bst import visualize_bst, find_node


# create a binary search tree
tree = BinarySearchTree()
graph = graphviz.Digraph()


import ipywidgets as widgets
from ipywidgets import BoundedIntText, Button, HTML, Layout, Tab, HBox, VBox, Output
from numpy.random import seed, randint

# create a tab widget
#-----------------------// output widgets //-----------------------------
out = Output()
tab = Tab(children=[out], layout=widgets.Layout(width='100%', height='auto'))
tab.set_title(0, 'Output')

#-----------------------// input widgets //-----------------------------
# input field for number of elements
num_elements = BoundedIntText(value=20,
                              min=1,
                              max=100,
                              step=1,
                              description='Number of elements:',
                              disabled=False,
                              layout=Layout(width='auto', height='auto'))
#print(type(num_elements.value))

#-----------------------// button widgets //-----------------------------

# insert button
insert_button = Button(
    description='Insert',
    button_style='success',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Insert',
    icon='plus',
    #style=widgets.ButtonStyle(button_color='lightgreen')
)


def insert_button_clicked(b):
    with out:
        # clear output
        out.clear_output()
        # insert value into BST
        tree.insert(num_elements.value)
        # visualize the tree
        graph = graphviz.Digraph()
        # visualize the tree
        visualize_bst(tree.root, graph)
        # show the tree
        display(graph)


# bind the button to the function
insert_button.on_click(insert_button_clicked)

# delete button
delete_button = Button(
    description='Delete',
    button_style='danger',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Delete',
    icon='minus')


def delete_button_clicked(b):
    with out:
        # clear the output
        out.clear_output()
        # delete the value
        tree.delete(num_elements.value)
        # visualize the tree
        graph = graphviz.Digraph()
        # visualize the tree
        visualize_bst(tree.root, graph)
        # show the tree
        display(graph)


# bind the button to the function
delete_button.on_click(delete_button_clicked)

# search button
search_button = Button(
    description='Search',
    button_style='info',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Search',
    icon='search')


def search_button_clicked(b):
    with out:
        # clear the output
        out.clear_output()

        # visualize the tree
        graph = graphviz.Digraph()

        # if the tree is empty
        if tree.root is None:
            # print error message
            print(msg2)
        # if the value is in the tree
        else:
            print(f"Searching for {num_elements.value}...")

            # if the value is not in the tree
            if not tree.search(num_elements.value):
                # print error message
                print(f"{num_elements.value} is not in the tree.")
                # visualize the tree
                visualize_bst(tree.root, graph)
                # show the tree
                display(graph)

            # if the value is in the tree
            else:
                # print success message
                print(f"{num_elements.value} is in the tree.")
                # visualize the tree
                visualize_bst(tree.root, graph)
                # find the node
                find_node(tree.root, graph, num_elements.value)
                # show the tree
                display(graph)


# bind the button to the function
search_button.on_click(search_button_clicked)

# random button
random_button = Button(
    description='Random',
    button_style='warning',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Random',
    icon='random')

seed(1)
random_n = randint(1, 50)


def random_button_clicked(b):
    with out:
        # clear the tree
        tree.clear()
        # clear the visualization
        graph = graphviz.Digraph()
        # clear the output
        out.clear_output()

        # fill the tree with random values and a random number of elements
        tree.fill_tree_random(num_elements=random_n, max_int=100)
        # visualize the tree
        visualize_bst(tree.root, graph)
        # show the tree
        display(graph)


# bind the button to the function
random_button.on_click(random_button_clicked)

# clear button
clear_button = Button(
    description='Clear',
    button_style='danger',  # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Clear',
    icon='trash')


def clear_button_clicked(b):
    with out:
        # clear the output
        out.clear_output()
        # clear the tree
        tree.clear()
        # print success message
        print("The tree has been cleared.")
        # reset the graph
        graph = graphviz.Digraph()


# bind the button to the function
clear_button.on_click(clear_button_clicked)

#-----------------------// error messages //-----------------------------
msg = """<p style="color:red">Error: Please enter a number between 1 and 100.</p>"""
msg2 = """<p style="color:red">Error: The tree is empty.</p>"""

#-----------------------// layout //-----------------------------
# create a horizontal box for the input widgets
input_widgets = HBox([
    num_elements, insert_button, delete_button, search_button, random_button,
    clear_button
])

# create a vertical box for the input widgets and the output widgets
widgets = VBox([input_widgets, tab])

# display the widgets
display(widgets)

#-----------------------// test //-----------------------------
