from avl import AVLTree

a = AVLTree()
for i in range(10):
    print(f"Inserting {i}...")
    a.insert(i)
    print(a)
    print("")


input("Press Enter to continue...")

for i in range(10):
    print(f"Deleting {i}...")
    a.delete_key(i)
    print(a)
    print("")


input("Press Enter to continue...")
    