class node:
    def __init__(self, key=None):
        self.key = key  # key of the node       // informaçao do nó
        self.left = None  # left child            // filho esquerdo
        self.right = None  # right child           // filho direito
        self.parent = None  # parent of the node    // pai do nó
        self.height = 1  # height of the node    // altura do nó


class AVLTree:
    def __init__(self):
        self.root = None  # root of the tree      // raiz da árvore

    def __repr__(self):
        if self.root is None:
            return ""

        content = "\n"  # to store the tree content
        current_node = [self.root]  # all nodes at current level
        current_height = self.root.height  # height of nodes at current level
        # variable sized separator between elements

        sep = " " * (2 ** (current_height - 1))

        while True:
            current_height += -1

            if len(current_node) == 0:
                break
            current_row = " "
            next_row = ""
            next_nodes = []

            if all(n is None for n in current_node):
                break

            for n in current_node:
                if n is None:
                    current_row += "   " + sep
                    next_row += "   " + sep
                    next_nodes.extend([None, None])
                    continue

                if n.key is not None:
                    buf = " " * int((5 - len(str(n.key))) / 2)
                    current_row += "%s%s%s" % (buf, str(n.key), buf) + sep
                else:
                    current_row += " " * 5 + sep

                if n.left is not None:
                    next_nodes.append(n.left)
                    next_row += " /" + sep
                else:
                    next_row += "  " + sep
                    next_nodes.append(None)

                if n.right is not None:
                    next_nodes.append(n.right)
                    next_row += "\ " + sep
                else:
                    next_row += " " + sep
                    next_nodes.append(None)

            content += (
                current_height * "   "
                + current_row
                + "\n"
                + current_height * "   "
                + next_row
                + "\n"
            )
            current_node = next_nodes
            sep = " " * int(len(sep) / 2)  # cut separator size in half
        return content

    def insert(self, key):
        # insert a node with key 'key' into the tree
        if self.root is None:
            self.root = node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, cur_node):
        if key < cur_node.key:
            if cur_node.left is None:  # se o filho esquerdo for vazio
                cur_node.left = node(key)  # cria um novo nó
                cur_node.left.parent = node  # o pai do novo nó é o nó atual
                self._inspect_insertion(cur_node.left)  # inspeciona a árvore
            else:
                # se o filho esquerdo não for vazio, chama a função recursivamente
                self._insert(key, cur_node.left)
        elif key > cur_node.key:  # se o valor for maior que o nó atual
            if cur_node.right is None:  # se o filho direito for vazio
                cur_node.right = node(key)
                cur_node.right.parent = cur_node

                # verifica se a árvore está balanceada
                self._inspect_insertion(cur_node.right)
            else:
                self._insert(key, cur_node.right)
        else:
            # se o valor já estiver na árvore
            print("key already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print("%s, h=%d" % (str(cur_node.key), cur_node.height))
            self._print_tree(cur_node.right)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, current_height):
        if cur_node is None:
            return current_height

        # se o nó atual for vazio, retorna a altura atual
        left_height = self._height(cur_node.left, current_height + 1)

        # se o nó atual for vazio, retorna a altura atual
        right_height = self._height(cur_node.right, current_height + 1)

        # retorna a maior altura
        return max(left_height, right_height)

    def find(self, key):
        # find the node with key 'key' in the tree
        if self.root is not None:
            return self._find(key, self.root)
        else:
            return None

    def _find(self, key, cur_node):
        # find the node with key 'key' in the tree
        if key is cur_node.key:
            return cur_node

        # if the key is less than the current node's key, go left
        elif key < cur_node.key and cur_node.left is not None:
            return self._find(key, cur_node.left)

        # if the key is greater than the current node's key, go right
        elif key > cur_node.key and cur_node.right is not None:
            return self._find(key, cur_node.right)

    def delete_key(self, key):
        return self.delete_node(self.find(key))

    def delete_node(self, node):
        # returns the node with min key in tree rooted at input node
        # retorna o nó com a menor chave na árvore
        if node is None or self.find(node.key) is None:
            print("Node to be deleted not found in the tree!")
            return None

        # returns the node with min key in tree rooted at input node
        def min_key_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0

            # se o filho esquerdo não for vazio, incrementa o número de filhos
            if n.left is not None:
                num_children += 1

            # se o filho direito não for vazio, incrementa o número de filhos
            if n.right is not None:
                num_children += 1

            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # case 1 (node has no children) // caso 1 (nó não tem filhos)
        if node_children == 0:
            if node_parent is not None:
                # remove reference to the node from the parent
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        # case 2 (node has a single child) // caso 2 (nó tem um único filho)
        if node_children == 1:
            # get the single child node
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if node_parent is not None:
                # replace the node to be deleted with its child
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # case 3 (node has two children) // caso 3 (nó tem dois filhos)
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = min_key_node(node.right)

            # copy the inorder successor's key to the node formerly
            # holding the key we wished to delete
            node.key = successor.key

            # delete the inorder successor now that it's key was
            # copied into the other node
            self.delete_node(successor)

            # exit function so we don't call the _inspect_deletion twice
            return

        if node_parent is not None:
            # fix the height of the parent of current node
            node_parent.height = 1 + max(
                self.get_height(node_parent.left), self.get_height(
                    node_parent.right)
            )

            # begin to traverse back up the tree checking if there are
            # any sections which now invalidate the AVL balance rules
            self._inspect_deletion(node_parent)

    def search(self, key):
        # find the node with key 'key' in the tree
        if self.root is not None:
            return self._search(key, self.root)

        else:
            return False

    def _search(self, key, cur_node):
        # if the key is less than the current node's key, go left
        if key == cur_node.key:
            return True

        # if the key is less than the current node's key, go left
        elif key < cur_node.key and cur_node.left is not None:
            return self._search(key, cur_node.left)

        # if the key is greater than the current node's key, go right
        elif key > cur_node.key and cur_node.right is not None:
            return self._search(key, cur_node.right)
        return False

    # Functions added for AVL...

    def _inspect_insertion(self, cur_node, path=[]):
        if cur_node.parent is None:
            return
        path = [cur_node] + path

        left_height = self.get_height(cur_node.parent.left)
        right_height = self.get_height(cur_node.parent.right)

        if abs(left_height - right_height) > 1:
            path = [cur_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    def _inspect_deletion(self, cur_node):
        if cur_node is None:
            return

        # update the height of the current node
        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)

        # the height of the current node is the max height of its children
        if abs(left_height - right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self, z, y, x):

        # left left case, so rotate right // caso esquerda esquerda, então rotacione para a direita
        if y == z.left and x == y.left:
            self._right_rotate(z)

        # left right case, so rotate left then right // caso esquerda direita, então rotacione para a esquerda e depois para a direita
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)

        # right right case, so rotate left // caso direita direita, então rotacione para a esquerda
        elif y == z.right and x == y.right:
            self._left_rotate(z)

        # right left case, so rotate right then left // caso direita esquerda, então rotacione para a direita e depois para a esquerda
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)

        else:
            raise Exception("Error in _rebalance_node")

    def _right_rotate(self, z):

        # set z as the root of the subtree
        sub_root = z.parent
        y = z.left
        t3 = y.right

        # perform rotation
        y.right = z
        z.parent = y
        z.left = t3

        # update heights
        if t3 is not None:
            t3.parent = z
        y.parent = sub_root

        # set the new root of the subtree
        if y.parent is None:
            self.root = y

        # set the new root of the subtree
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def _left_rotate(self, z):

        # set z as the root of the subtree
        sub_root = z.parent
        y = z.right
        t2 = y.left

        # perform rotation
        y.left = z
        z.parent = y
        z.right = t2

        # update heights
        if t2 is not None:
            t2.parent = z
        y.parent = sub_root

        # set the new root of the subtree
        if y.parent is None:
            self.root = y

        # set the new root of the subtree
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def get_height(self, cur_node):
        # return the height of the node // retorna a altura do nó
        if cur_node is None:
            return 0
        return cur_node.height

    def taller_child(self, cur_node):
        # return the taller child of the current node // retorna o filho mais alto do nó atual
        left = self.get_height(cur_node.left)

        # if the left child is taller than the right child, return the left child // se o filho esquerdo for mais alto que o filho direito, retorne o filho esquerdo
        right = self.get_height(cur_node.right)

        # if the left child is taller than the right child, return the left child // se o filho esquerdo for mais alto que o filho direito, retorne o filho esquerdo
        return cur_node.left if left >= right else cur_node.right


a = AVLTree()
for i in range(10):
    print("Inserting: ", i)
    a.insert(i)
    print(a)

for i in range(10):
    print("Deleting: ", i)
    a.delete_key(i)
    print(a)
