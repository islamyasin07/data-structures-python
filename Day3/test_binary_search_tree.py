from binary_search_tree import BinarySearchTree

if __name__ == "__main__":
    smp = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        smp.insert(val)

    # Inorder Traversal
    inorder_result = []
    smp.inorder(smp.root, inorder_result)
    print("Inorder traversal :")
    print(inorder_result)  

    # Preorder Traversal
    preorder_result = []
    smp.preorder(smp.root, preorder_result)
    print("\nPreorder traversal :")
    print(preorder_result)  

    # Postorder Traversal
    postorder_result = []
    smp.postorder(smp.root, postorder_result)
    print("\nPostorder traversal ")
    print(postorder_result) 

    print("\nSearching for 60:")
    print(smp.search(60)) 

    print("Searching for 25:")
    print(smp.search(25))  
