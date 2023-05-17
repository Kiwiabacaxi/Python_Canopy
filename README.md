# Visualizing Search and Sorting Algorithms with Python

## Introduction

This repository contains implementations of Binary Trees, along with visualizations of the algorithms used for searching and sorting with these structures.

## Binary Search Tree
<a target="_blank" href="https://colab.research.google.com/github/Kiwiabacaxi/Python_Canopy/blob/main/python_canopy/BST/BSTree.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Binary Search Tree (BST) is a binary tree data structure where each node has at most two children, and the left subtree of a node contains only values less than the node's value, while the right subtree contains only values greater than the node's value.

This ordering property ensures that the worst-case time complexity for search, insertion, and deletion operations is O(h), where h is the height of the tree. In a well-balanced binary search tree, the height is O(log n), where n is the number of elements in the tree.

In this repository, we provide an implementation of the Binary Search Tree data structure in Python, along with visualizations of the algorithms used for searching and sorting with the Binary Search Tree.

## AVL Tree

An AVL Tree is a self-balancing binary search tree, where the height of the left and right subtrees of any node differ by at most one. This balancing property ensures that the worst-case time complexity for operations such as insertion, deletion, and searching is O(log n), where n is the number of elements in the tree.

In this repository, we provide an implementation of the AVL Tree data structure in Python, along with a visualization of the AVL Tree balancing algorithm. The visualization allows you to see how the AVL Tree self-balances after an insertion or deletion operation.

## Red & Black Tree

A Red-Black Tree is a self-balancing binary search tree data structure. Each node in the tree is colored either red or black, and the tree is balanced using a set of color and structure rules. The rules state that the root must be black, every leaf (nil) node must be black, and if a node is red, its children must be black. Additionally, the path from the root to every leaf must contain the same number of black nodes.

This balancing property ensures that the worst-case time complexity for operations such as insertion, deletion, and searching is O(log n), where n is the number of elements in the tree. Red-Black Trees are commonly used in computer science for efficient searching and sorting of large amounts of data.

In this repository, we provide an implementation of the Red-Black Tree data structure in Python, along with visualizations of the algorithms used for searching and sorting with the Red-Black Tree. The visualizations allow you to see how the tree self-balances after an insertion or deletion operation.

## B-Tree

A B-Tree is a self-balancing tree data structure that can store large amounts of data on disk or in memory. The B-Tree is used in file systems and databases where large amounts of data need to be stored and retrieved quickly.

In this repository, we provide an implementation of the B-Tree data structure in Python, along with visualizations of the algorithms used for searching and sorting with the B-Tree. The visualizations allow you to see how the B-Tree splits and merges nodes to maintain balance and efficiency.

## How to Use

To use the AVL Tree or B-Tree implementations and visualizations in this repository, simply clone the repository and run the Python files, or use the jupyter notebooks.

## Conclusion

This repository provides implementations and visualizations of the AVL Tree and B-Tree data structures in Python. These structures are commonly used in computer science for efficient searching and sorting of large amounts of data. The visualizations provided in this repository allow you to see how these algorithms work and how the trees self-balance to maintain efficiency.

# Visualização de Algoritmos de Busca e Ordenação com Python

## Introdução

Este repositório contém implementações das estruturas de dados Arvores binarias, juntamente com visualizações dos algoritmos usados para busca e ordenação com essas estruturas.

## Árvore Binária de Busca

Árvore Binária de Busca (BST) é uma estrutura de dados de árvore binária onde cada nó tem no máximo dois filhos, e a subárvore esquerda de um nó contém apenas valores menores que o valor do nó, enquanto a subárvore direita contém apenas valores maiores que o valor do nó.

Essa propriedade de ordenação garante que a complexidade do pior caso para operações de busca, inserção e exclusão seja O(h), onde h é a altura da árvore. Em uma árvore binária de busca bem balanceada, a altura é O(log n), onde n é o número de elementos na árvore.

Neste repositório, fornecemos uma implementação da estrutura de dados Árvore Binária de Busca em Python, juntamente com visualizações dos algoritmos usados para busca e ordenação com a Árvore Binária de Busca.

## Árvore AVL

Uma Árvore AVL é uma árvore de busca binária auto-balanceável, onde a altura das subárvores esquerda e direita de qualquer nó diferem em no máximo um. Essa propriedade de balanceamento garante que a complexidade do pior caso para operações como inserção, exclusão e busca seja O(log n), onde n é o número de elementos na árvore.

Neste repositório, fornecemos uma implementação da estrutura de dados Árvore AVL em Python, juntamente com uma visualização do algoritmo de balanceamento da Árvore AVL. A visualização permite que você veja como a Árvore AVL se auto-balanceia após uma operação de inserção ou exclusão.

## Árvore rubro-negra (R&B)

Uma Árvore R&B (Red-Black Tree) é uma estrutura de dados de árvore binária auto-balanceável, semelhante a uma Árvore Binária de Busca, mas com a adição de um atributo de cor em cada nó. Cada nó é colorido em vermelho ou preto, seguindo algumas regras de coloração que garantem o balanceamento da árvore.

Essa propriedade de balanceamento garante que a complexidade do pior caso para operações de busca, inserção e exclusão é O(log n), onde n é o número de elementos na árvore. Além disso, a Árvore R&B garante que a altura da árvore nunca exceda 2 * log(n + 1), o que garante a eficiência na realização das operações.

As regras de coloração em uma Árvore R&B incluem garantir que nenhum nó vermelho tenha um filho vermelho, que a raiz sempre seja preta e que todas as folhas (nós sem filhos) sejam pretas. Além disso, a Árvore R&B garante que o caminho mais longo da raiz até uma folha nunca seja mais do que duas vezes o caminho mais curto da raiz até outra folha.

Neste repositório, podemos fornecer uma implementação da estrutura de dados Árvore R&B em Python, juntamente com visualizações dos algoritmos usados para busca e ordenação com a Árvore R&B.

## Árvore B

Uma Árvore B é uma estrutura de dados de árvore auto-balanceável que pode armazenar grandes quantidades de dados em disco ou na memória. A Árvore B é usada em sistemas de arquivos e bancos de dados
