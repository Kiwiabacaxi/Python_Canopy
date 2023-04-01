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
    if tree != None:
        # draw the circle
        circle = Circle(Point(x, y), 0.4 * level)
        circle.setFill("red")
        circle.draw(win)
        # draw the text
        text = Text(Point(x, y), tree.key)
        text.draw(win)
        # draw the left child
        drawNode(tree.left, win, x - 0.8 * level, y - 1, level - 1)
        # draw the right child
        drawNode(tree.right, win, x + 0.8 * level, y - 1, level - 1)
        # draw the rotate
        if rotate == "left":
            line = Line(Point(x + 0.4 * level, y - 0.4 * level), Point(x + 0.8 * level, y - 1))
            line.draw(win)
        elif rotate == "right":
            line = Line(Point(x - 0.4 * level, y - 0.4 * level), Point(x - 0.8 * level, y - 1))
            line.draw(win)
        
# main
def main():
    # create a window
    win = GraphWin("AVL Tree", 600, 600)
    win.setCoords(0, 0, 10, 10)
    # create a tree
    tree = AVLTree()
    # insert the nodes
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert(25)
    # draw the tree
    drawTree(tree, win)
    # rotate
    tree.rotateLeft(tree.root)
    tree.rotateRight(tree.root)
    # draw the rotate
    drawRotate(tree.root, win, 5, 9, 4, "left")
    drawRotate(tree.root, win, 5, 9, 4, "right")
    # wait for a mouse click
    win.getMouse()
    win.close()

main()