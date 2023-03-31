class node:
    def __init__(self, key):
        self.key = key          # key of the node       // informaçao do nó
        self.left = None        # left child            // filho esquerdo
        self.right = None       # right child           // filho direito
        self.parent = None      # parent of the node    // pai do nó
        self.height = 1         # height of the node    // altura do nó

    def __str__(self):
        # return the key of the node // retorna a chave do nó em forma de string
        return str(self.key)


class AVLTree:
    def __init__(self):
        self.root = None  # root of the tree      // raiz da árvore

    def __repr__(self):
        if self.root is None:
            return 'Empty tree'  # se a árvore estiver vazia retorna 'Empty tree'

        content = '\n'  # to store the tree content
        current_node = [self.root]  # all nodes at current level
        current_height = self.root.height  # height of nodes at current level
        # variable sized separator between elements
        sep = ' ' * (2 ** (current_height - 1))
        while True:
            if all(n is None for n in current_node):
                break

            if len(current_node) == 0:
                break

            current_height += -1
            current_row = ' '
            next_row = ''
            next_nodes = []

            for n in current_node:
                if n is None:
                    current_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.key != None:
                    buf = ' ' * int((5 - len(str(n.key))) / 2)
                    current_row += '%s%s%s' % (buf, n.key, buf) + sep

                else:
                    current_row += ' '*5+sep

                if n.left != None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right != None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (current_height*'   '+current_row +
                        '\n'+current_height*'   '+next_row+'\n')
            sep = ' '*int(len(sep)/2)  # cut separator size in half
            current_node = next_nodes

        return content

    def insert(self, key):
        # insert a node with key 'key' into the tree // insere um nó com chave 'key' na árvore
        if self.root == None:
            self.root = node(key)
        else:
            self._insert(self.root, key)

#   def _insert(self, current_node, key):
    def _insert(self, key, current_node):
        if key < current_node.key:
            if current_node.left == None:                  # se o filho esquerdo for vazio
                current_node.left = node(key)              # cria o nó
                current_node.left.parent = current_node   # define o pai do nó
                # verifica se a árvore está balanceada
                self._inspect_insertion(current_node.left)
            else:
                # se o filho esquerdo não for vazio, chama a função novamente
                self._insert(key, current_node.left)

        elif key > current_node.key:
            if current_node.right == None:                 # se o filho direito for vazio
                current_node.right = node(key)             # cria o nó
                current_node.right.parent = current_node  # define o pai do nó
                # verifica se a árvore está balanceada
                self._inspect_insertion(current_node.right)
            else:
                self._insert(key, current_node.right)
                
        else:
            # se a chave já existir na árvore
            print(" The key already exists in the tree ")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left)
            print('%s, h=%d' % (str(current_node.key), current_node.height))
            self._print_tree(current_node.right)

    def height(self):
        if self.root != None:
            return self._height(self.node, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node == None:  # empty node // se o nó for vazio
            return current_height

        # left subtree // subárvore esquerda
        left_height = self._height(current_node.left, current_height + 1)

        # right subtree // subárvore direita
        right_height = self._height(current_node.right, current_height + 1)

        # retorna a maior altura entre a subárvore esquerda e a subárvore direita
        return max(left_height, right_height)

    def find(self, key):
        # find the node with key 'key' // encontra o nó com chave 'key'
        if self.root != None:
            return self._find(key, self.root)
        else:
            return None

    def _find(self, key, current_node):
        # se a chave for igual a chave do nó atual
        if key == current_node.key:
            return current_node

        # se a chave for menor que a chave do nó atual e o filho esquerdo não for vazio
        elif key < current_node.key and current_node.left != None:
            return self._find(key, current_node.left)

        # se a chave for maior que a chave do nó atual e o filho direito não for vazio
        elif key > current_node.key and current_node.right != None:
            return self._find(key, current_node.right)

    def delete_value(self, key):
        return self.delete_node(self.find(key))

    def delete_node(self, node):
        # returns the node or None if the key is not found // retorna o nó ou None se a chave não for encontrada
        if node == None or self.find(node.key) == None:
            print(" Node to be deleted not found in the tree ")
            return None

        # returns the node with the minimum value // retorna o nó com o valor mínimo
        def min_value_node(a):

            current = a

            # loop para encontrar o nó com o valor mínimo
            while current.left != None:
                current = current.left
            return current

        # returns the number of children for the specified node // retorna o número de filhos para o nó especificado
        def num_children(a):
            num_children = 0

            # se o filho esquerdo não for vazio
            if a.left != None:
                num_children += 1

            # se o filho direito não for vazio
            if a.right != None:
                num_children += 1

            return num_children

        # get the parent of the node to be deleted // obtém o pai do nó a ser excluído
        node_parent = node.parent
        # get the number of children of the node to be deleted // obtém o número de filhos do nó a ser excluído
        node_children = num_children(node)

        # case 1 (node has no children) // caso 1 (nó não tem filhos)
        if node_children == 0:

            # se o nó não for a raiz
            if node_parent != None:
                # removes the reference to the node from the parent // remove a referência ao nó do pai
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None

            # se o nó for a raiz
            else:
                self.root = None

        # case 2 (node has a single child) // caso 2 (nó tem um único filho)
        if node_children == 1:

            # get the single child node // obtém o nó filho único
            if node.left != None:
                child = node.left
            else:
                child = node.right

            # se o nó não for a raiz
            if node_parent != None:

                # se o nó for o filho esquerdo do pai
                if node_parent.left == node:
                    # define o filho esquerdo do pai como o filho do nó
                    node_parent.left = child
                else:
                    node_parent.right = child

            # se o nó for a raiz
            else:
                self.root = child

        # case 3 (node has two children) // caso 3 (nó tem dois filhos)
        if node_children == 2:

            # get the inorder successor of the deleted node // obtém o sucessor em ordem do nó excluído
            sucessor = min_value_node(node.right)

            # copia o valor do sucessor para o nó
            node.key = sucessor.key

            # deleta o sucessor
            self.delete_node(sucessor)

            # exit function so we don't call _inspect_deletion twice // sai da função para não chamarmos _inspect_deletion duas vezes
            return

        # verifica se a árvore está balanceada
        if node_parent != None:
            # fix the height of the parent // atualiza a altura do pai

            node_parent.height = 1 + \
                max(self.get_height(node_parent.left),
                    self.get_height(node_parent.right))

            # begin to inspect the tree for balance // começa a inspecionar a árvore para o equilíbrio
            self._inspect_deletion(node_parent)

    def search(self, key):
        # search the tree for a node with the key 'key' // pesquisa a árvore por um nó com a chave 'key'
        if self.root != None:
            return self._search(key, self.root)
        # se a raiz for vazia
        else:
            return False

    def _search(self, key, current_node):

        # if the key is equal to the key of the current node // se a chave for igual à chave do nó atual
        if key == current_node.key:
            return True

        # if the key is less than the key of the current node // se a chave for menor que a chave do nó atual
        elif key < current_node.key and current_node.left != None:
            return self._search(key, current_node.left)

        # if the key is greater than the key of the current node // se a chave for maior que a chave do nó atual
        elif key > current_node.key and current_node.right != None:
            return self._search(key, current_node.right)

        return False

    def _inspect_insertion(self, current_node, path=[]):

        if current_node.parent == None:
            return
        path = [current_node] + path

        left_height = self.get_height(current_node.parent.left)
        right_height = self.get_height(current_node.parent.right)

        if abs(left_height - right_height) > 1:
            path = [current_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1 + current_node.height
        if new_height > current_node.parent.height:
            current_node.parent.height = new_height

        self._inspect_insertion(current_node.parent, path)

    def _inspect_deletion(self, current_node):
        if current_node == None:
            return

        # atualiza a altura do nó
        left_height = self.get_height(current_node.left)
        right_height = self.get_height(current_node.right)

        # the height of the current node is the maximum height of its children plus one // a altura do nó atual é a altura máxima de seus filhos mais um
        if abs(left_height - right_height) > 1:
            y = self.taller_child(current_node)
            x = self.taller_child(y)
            self._rebalance_node(current_node, y, x)
            return

        self._inspect_deletion(current_node.parent)

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

        # set up
        aux = z.parent
        y = z.left
        t3 = y.right

        # rotation
        y.right = z
        z.parent = y
        z.left = t3
        if t3 != None:
            t3.parent = z

        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # set new root
        if aux != None:
            if aux.left == z:
                aux.left = y
            else:
                aux.right = y
        y.parent = aux

        if z == self.root:
            self.root = y
            y.parent = None

    def _left_rotate(self, z):

        # set up
        aux = z.parent
        y = z.right
        t2 = y.left

        # rotation
        y.left = z
        z.parent = y
        z.right = t2
        if t2 != None:
            t2.parent = z

        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # set new root
        if aux != None:
            if aux.left == z:
                aux.left = y
            else:
                aux.right = y
        y.parent = aux

        if z == self.root:
            self.root = y
            y.parent = None

    def get_height(self, node):
        # return the height of the node // retorna a altura do nó
        if node == None:
            return -1
        else:
            return node.height

    def taller_child(self, node):

        # left receives the height of the left child // esquerda recebe a altura do filho esquerdo
        left = self.get_height(node.left)
        
        # right receives the height of the right child // direita recebe a altura do filho direito
        right = self.get_height(node.right)

        # return the child with the greater height // retorna o filho com a maior altura
        return node.left if left >= right else node.right


""" a = AVLTree()
for i in range(10):
    print(f"Inserting {i}...")
    a.insert(i)
    print(a)
    print("")

for i in range(10):
    print(f"Deleting {i}...")
    a.delete(i)
    print(a)
    print("")
     """

a = AVLTree()
for i in range(10):
    print("Inserting: ", i)
    a.insert(i)
    print(a)

for i in range(10):
    print("Deleting: ", i)
    a.delete_value(i)
    print(a)
