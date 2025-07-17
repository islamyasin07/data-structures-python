class Node:
    def __init__(self, data):
        self.data = data     
        self.left = None    
        self.right = None     

class BinarySearchTree:
    def __init__(self):
        self.root = None    

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)    
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.data:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)

    def preorder(self, node, result):
        if node:
            result.append(node.data)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.data)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False  
        if current.data == value:
            return True 
        elif value < current.data:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)
