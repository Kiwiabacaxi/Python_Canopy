import graphviz
from ipywidgets.widgets.interaction import display
from AVL_tree import AVLTree
from graphviz_AVL_tree import AVLTreeGraph

# create AVL search tree
tree = AVLTreeGraph()
graph = graphviz.Digraph()

import ipywidgets as widgets
from ipywidgets import HBox, Layout, VBox, interact, interactive, fixed, interact_manual
from numpy.random import seed, randint


# function to create a tab widget
def create_tab_widget():
    # create a tab widget
    #-----------------------// output widgets //-----------------------------
    out = widgets.Output()
    tab = widgets.Tab(children=[out],
                      layout=widgets.Layout(width='100%', height='auto'))
    tab.set_title(0, 'Output')
    return tab, out


# function to create a button widget
def create_button_widget(description, button_style, tooltip, icon):
    button = widgets.Button(
        description=description,
        button_style=
        button_style,  # 'success', 'info', 'warning', 'danger' or ''
        tooltip=tooltip,
        icon=icon,
        #style=widgets.ButtonStyle(button_color='lightgreen')
    )
    return button


# function to create an input widget
def create_input_widget(value, min, max, step, description, disabled, tooltip):
    input_widget = widgets.IntText(value=value,
                                   min=min,
                                   max=max,
                                   step=step,
                                   description=description,
                                   disabled=disabled,
                                   tooltip=tooltip,
                                   layout=widgets.Layout(width='auto',
                                                         height='auto'))
    return input_widget


# function to create a text widget
def create_text_widget(value, description, disabled):
    text_widget = widgets.Text(value=value,
                               description=description,
                               disabled=disabled,
                               layout=widgets.Layout(width='auto',
                                                     height='auto'))
    return text_widget


#-----------------------// input widgets //-----------------------------
# input field for number of elements
num_elements = create_input_widget(
    value=20,
    min=1,
    max=100,
    step=1,
    description='Number of elements:',
    disabled=False,
    tooltip='Number of elements to insert/search into the tree.',
)

# input field for max integer
max_int = create_input_widget(
    value=100,
    min=1,
    max=10000,
    step=1,
    description='Max integer:',
    disabled=False,
    tooltip='Maximum integer to insert/search into the tree.',
)

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
                                     button_style='danger',
                                     tooltip='Delete',
                                     icon='minus')

# random button
random_button = create_button_widget(description='Random',
                                     button_style='warning',
                                     tooltip='Random',
                                     icon='random')

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
        # insert value into AVL
        tree.insert(num_elements.value)
        # visualize the tree
        graph = graphviz.Digraph()
        # visualize the tree
        tree.visualize_avl(tree.root, graph)
        # show the tree
        display(graph)


# bind the button to the function
insert_button.on_click(insert_button_clicked)


# search button
def search_button_clicked(b):
    with out:
        # clear the output
        out.clear_output()

        # visualize the tree
        graph = graphviz.Digraph()

        # if the tree is empty
        if tree.root is None:
            # print error message
            print("The tree is empty.")
        # if the value is in the tree
        else:
            print(f"Searching for {num_elements.value}...")

            # if the value is not in the tree
            if not tree.search(num_elements.value):
                # print error message
                print(f"{num_elements.value} is not in the tree.")
                # visualize the tree
                tree.visualize_avl(tree.root, graph)
                # show the tree
                display(graph)

            # if the value is in the tree
            else:
                # print success message
                print(f"{num_elements.value} is in the tree.")
                # visualize the tree
                tree.visualize_avl(tree.root, graph)
                # find the node
                tree.find_node(tree.root, graph, num_elements.value)
                # show the tree
                display(graph)


# bind the button to the function
search_button.on_click(search_button_clicked)


# delete button
def delete_button_clicked(b):
    with out:
        # clear output
        out.clear_output()
        # delete value from AVL
        tree.delete(int(search_value.value))
        # visualize the tree
        graph = graphviz.Digraph()
        # visualize the tree
        tree.visualize_avl(tree.root, graph)
        # show the tree
        display(graph)


# bind the button to the function
delete_button.on_click(delete_button_clicked)


def random_button_clicked(b):
    with out:
        # clear the tree
        tree.clear()
        # clear the visualization
        graph = graphviz.Digraph()
        # clear the output
        out.clear_output()

        # fill the tree with random values and a random number of elements
        tree.fill_tree_random(size=num_elements.value,
                              max_value=max_int.value)
        # visualize the tree
        tree.visualize_avl(tree.root, graph)
        # show the tree
        display(graph)


# bind the button to the function
random_button.on_click(random_button_clicked)


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
        tree.visualize_avl(tree.root, graph)
        # show the tree
        display(graph)


# bind the button to the function
clear_button.on_click(clear_button_clicked)

# -----------------------------// HBox and VBox widgets //--------------------------
# create a horizontal box widget
input_widgets = HBox([
    num_elements, max_int, insert_button, search_button, delete_button,
    random_button, clear_button
])

widgets = VBox([input_widgets, tab])

# create a vertical box widget


# function to display the widgets
def display_widgets():
    display(widgets)
