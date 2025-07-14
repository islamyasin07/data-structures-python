class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        #Start with an empty stack
        self.top = None

    #Add a new item
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    #Remove and return the top item from the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    #View the top item without removing it
    def invs(self):
        if self.is_empty():
            raise IndexError("empty stack")
        return self.top.value

    #Check if the stack is empty
    def is_empty(self):
        return self.top is None

    #Return the number of items in the stack
    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    # Print the stack from top to bottom
    def display(self):
        current = self.top
        print("Stack (top -> end):", end=" ")
        while current:
            print(f"[{current.value}]", end=" -> ")
            current = current.next
        print("None")
