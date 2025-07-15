class Node:
    def __init__(self, value):
        #Store the node value
        self.value = value
        #Point to the next node - Default is the Edge - none
        self.next = None


#This class handles the Singly Linked List operations
class SinglyLinkedList:
    def __init__(self):
        # Start with an empty list (no head)
        self.head = None

    #Add a new value to the end of the list
    def add(self, value):
        new_node = Node(value)
        #If list is empty, make this the first node
        if self.head is None:
            self.head = new_node
        else:
            #Go to the last node
            current = self.head
            while current.next:
                current = current.next
            #Add the new node at the end
            current.next = new_node

    #Show all elements in the list in order
    def display(self):
        current = self.head
        elements = []
        #Going through all nodes and get their values
        while current:
            elements.append(str(current.value))
            current = current.next
        #Print values with arrows for each node 
        print(" -> ".join(elements) + " -> None")

    #Remove a node that has a specific value
    def remove(self, value):
        #If list is empty -> do nothing
        if self.head is None:
            return
        #If the first node has the value -> remove it
        if self.head.value == value:
            self.head = self.head.next
            return
        #Search for the node to remove
        #Start from the head
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        #If found -> skip the node to remove it
        if current.next:
            current.next = current.next.next

    #Count how many nodes are in the list
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    #Get the value of the node at a specific index
    def get_at(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            current = current.next
            count += 1
        #If index is invalid -> raise error
        raise IndexError("Out of Borders !")
