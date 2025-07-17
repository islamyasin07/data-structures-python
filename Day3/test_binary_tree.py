from binary_tree import Node, BinaryTree

if __name__ == "__main__":
    root = Node("A")                
    root.left = Node("B")             
    root.right = Node("C")            
    root.left.left = Node("D")        
    root.left.right = Node("E")       
    root.right.right = Node("F")     


    tree = BinaryTree(root)

    # Preorder Traversal
    preorder_result = []
    tree.preorder(tree.root, preorder_result)
    print("Preorder traversal :")
    print(preorder_result)  

    # Inorder Traversal
    inorder_result = []
    tree.inorder(tree.root, inorder_result)
    print("\nInorder traversal :")
    print(inorder_result) 

    # Postorder Traversal
    postorder_result = []
    tree.postorder(tree.root, postorder_result)
    print("\nPostorder traversal :")
    print(postorder_result)  
