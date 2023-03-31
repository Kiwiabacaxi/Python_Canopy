from avl import *

a = AVLTree()
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
    