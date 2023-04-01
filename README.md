# Visualizing Search and Sorting Algorithms with Python

## Introduction

This repository contains implementations of the AVL Tree and B-Tree data structures in Python, along with visualizations of the algorithms used for searching and sorting with these structures.

## Binary Search Tree

Binary Search Tree (BST) is a binary tree data structure where each node has at most two children, and the left subtree of a node contains only values less than the node's value, while the right subtree contains only values greater than the node's value.

This ordering property ensures that the worst-case time complexity for search, insertion, and deletion operations is O(h), where h is the height of the tree. In a well-balanced binary search tree, the height is O(log n), where n is the number of elements in the tree.

In this repository, we provide an implementation of the Binary Search Tree data structure in Python, along with visualizations of the algorithms used for searching and sorting with the Binary Search Tree.

## AVL Tree

An AVL Tree is a self-balancing binary search tree, where the height of the left and right subtrees of any node differ by at most one. This balancing property ensures that the worst-case time complexity for operations such as insertion, deletion, and searching is O(log n), where n is the number of elements in the tree.

In this repository, we provide an implementation of the AVL Tree data structure in Python, along with a visualization of the AVL Tree balancing algorithm. The visualization allows you to see how the AVL Tree self-balances after an insertion or deletion operation.

## B-Tree

A B-Tree is a self-balancing tree data structure that can store large amounts of data on disk or in memory. The B-Tree is used in file systems and databases where large amounts of data need to be stored and retrieved quickly.

In this repository, we provide an implementation of the B-Tree data structure in Python, along with visualizations of the algorithms used for searching and sorting with the B-Tree. The visualizations allow you to see how the B-Tree splits and merges nodes to maintain balance and efficiency.

## How to Use

To use the AVL Tree or B-Tree implementations and visualizations in this repository, simply clone the repository and run the Python files.

For the AVL Tree visualization, run the avl_visualization.py file. This will open a window displaying the AVL Tree balancing algorithm.

For the B-Tree visualizations, run the b_tree_search_visualization.py or b_tree_sort_visualization.py files, depending on whether you want to visualize the search or sorting algorithm. These files will open windows displaying the B-Tree search or sorting algorithm.

## Conclusion

This repository provides implementations and visualizations of the AVL Tree and B-Tree data structures in Python. These structures are commonly used in computer science for efficient searching and sorting of large amounts of data. The visualizations provided in this repository allow you to see how these algorithms work and how the trees self-balance to maintain efficiency.

# Visualização de Algoritmos de Busca e Ordenação com Python

## Introdução

Este repositório contém implementações das estruturas de dados Árvore AVL e Árvore B em Python, juntamente com visualizações dos algoritmos usados para busca e ordenação com essas estruturas.

## Árvore Binária de Busca

Árvore Binária de Busca (BST) é uma estrutura de dados de árvore binária onde cada nó tem no máximo dois filhos, e a subárvore esquerda de um nó contém apenas valores menores que o valor do nó, enquanto a subárvore direita contém apenas valores maiores que o valor do nó.

Essa propriedade de ordenação garante que a complexidade do pior caso para operações de busca, inserção e exclusão seja O(h), onde h é a altura da árvore. Em uma árvore binária de busca bem balanceada, a altura é O(log n), onde n é o número de elementos na árvore.

Neste repositório, fornecemos uma implementação da estrutura de dados Árvore Binária de Busca em Python, juntamente com visualizações dos algoritmos usados para busca e ordenação com a Árvore Binária de Busca.

## Árvore AVL

Uma Árvore AVL é uma árvore de busca binária auto-balanceável, onde a altura das subárvores esquerda e direita de qualquer nó diferem em no máximo um. Essa propriedade de balanceamento garante que a complexidade do pior caso para operações como inserção, exclusão e busca seja O(log n), onde n é o número de elementos na árvore.

Neste repositório, fornecemos uma implementação da estrutura de dados Árvore AVL em Python, juntamente com uma visualização do algoritmo de balanceamento da Árvore AVL. A visualização permite que você veja como a Árvore AVL se auto-balanceia após uma operação de inserção ou exclusão.

## Árvore B

Uma Árvore B é uma estrutura de dados de árvore auto-balanceável que pode armazenar grandes quantidades de dados em disco ou na memória. A Árvore B é usada em sistemas de arquivos e bancos de dados
