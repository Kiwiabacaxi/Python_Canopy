# animate the avl tree using graphic

from graphics import *
from avl import *

# draw the tree
def drawTree(tree, win):
    drawNode(tree.root, win, 5, 9, 4)

# draw the node
def drawNode(node, win, x, y, level):
    if node != None:
        # draw the circle
        circle = Circle(Point(x, y), 0.4 * level)
        circle.setFill("red")
        circle.draw(win)
        # draw the text
        text = Text(Point(x, y), node.key)
        text.draw(win)
        # draw the left child
        drawNode(node.left, win, x - 0.8 * level, y - 1, level - 1)
        # draw the right child
        drawNode(node.right, win, x + 0.8 * level, y - 1, level - 1)

# draw the rotate
def drawRotate(tree, win, x, y, level, rotate):
    
