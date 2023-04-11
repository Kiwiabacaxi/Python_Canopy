import graphviz
from bin_search_tree import binarySearchTree
from graphviz_bst import visualize_bst, find_node

# create a binary search tree
tree = binarySearchTree()
graph = graphviz.Digraph()

import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual
from numpy.random import seed, randint

# function to create a tab widget
def create_tab_widget():
    # create a tab widget
    #-----------------------// output widgets //-----------------------------
    out = widgets.Output()
    tab = widgets.Tab(children=[out], layout=widgets.Layout(width='100%', height='auto'))
    tab.set_title(0, 'Output')
    return tab, out

# function to create a button widget
def create_button_widget(description, button_style, tooltip, icon):
    button = widgets.Button(
        description=description,
        button_style=button_style,  # 'success', 'info', 'warning', 'danger' or ''
        tooltip=tooltip,
        icon=icon,
        #style=widgets.ButtonStyle(button_color='lightgreen')
    )
    return button

# function to create an input widget
def create_input_widget(value, min, max, step, description, disabled):
    input_widget = widgets.BoundedIntText(value=value,
                                          min=min,
                                          max=max,
                                          step=step,
                                          description=description,
                                          disabled=disabled,
                                          layout=widgets.Layout(width='auto', height='auto'))
    return input_widget

# function to create a text widget
def create_text_widget(value, description, disabled):
    text_widget = widgets.Text(value=value,
                               description=description,
                               disabled=disabled,
                               layout=widgets.Layout(width='auto', height='auto'))
    return text_widget


#-----------------------// input widgets //-----------------------------
# input field for number of elements
num_elements = create_input_widget(value=20,
                                      min=1,
                                        max=100,
                                        step=1,
                                        description='Number of elements:',
                                        disabled=False)

#-----------------------// button widgets //-----------------------------
# insert button
insert_button = create_button_widget(description='Insert',
                                        button_style='success',
                                        tooltip='Insert',
                                        icon='plus')

# search button
search_button = create_button_widget(description='Search',
                                        button_style='info',
                                        tooltip='Search',
                                         icon='search')

# delete button
delete_button = create_button_widget(description='Delete',
                                            button_style='warning',
                                            tooltip='Delete',
                                            icon='minus')

# clear button
clear_button = create_button_widget(description='Clear',
                                             button_style='danger',
                                                tooltip='Clear',
                                                icon='trash')

#-----------------------// text widgets //-----------------------------
# text field for search value
search_value = create_text_widget(value='',
                                        description='Search value:',
                                        disabled=False)

#-----------------------// tab widget //-----------------------------
tab, out = create_tab_widget()

#-----------------------// button functions //-----------------------------
# insert button
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

# search button
def search_button_clicked(b):
    with out:
        # clear output
        out.clear_output()
        # search value in BST
        node = find_node(tree.root, int(search_value.value))
        # visualize the tree
        graph = graphviz.Digraph()
        # visualize the tree
        visualize_bst(tree.root, graph, node)
        # show the tree
        display(graph)
        
# bind the button to the function
search_button.on_click(search_button_clicked)

# delete button
def delete_button_clicked(b):
    with out:
        # clear output
        out.clear_output()
        # delete value from BST
        tree.delete(int(search_value.value))
        # visualize the tree
        graph = graphviz.Digraph()
        # visualize the tree
        visualize_bst(tree.root, graph)
        # show the tree
        display(graph)
        
# bind the button to the function
delete_button.on_click(delete_button_clicked)

# clear button
def clear_button_clicked(b):
    with out:
        # clear output
        out.clear_output()
        # clear the tree
        tree.clear()
        # visualize the tree
        graph = graphviz.Digraph()
        # visualize the tree
        visualize_bst(tree.root, graph)
        # show the tree
        display(graph)

# bind the button to the function
clear_button.on_click(clear_button_clicked)

#-----------------------// display widgets //-----------------------------
# display the widgets
display(num_elements)
display(insert_button)
display(search_value)
display(search_button)
display(delete_button)
display(clear_button)
display(tab)

 