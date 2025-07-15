class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #Add a new node at the end of the list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            #Go to the last node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    #Remove node by value
    def remove(self, value):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current and current.value != value:
            current = current.next

        if current is None:
            print("Value not found")
            return

        if current.prev is None:
            self.head = current.next
            if self.head:
                self.head.prev = None
        else:
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

    #Show all values from start to end
    def display_forward(self):
        current = self.head
        print("Forward: ", end="")
        while current:
            print(f"[{current.value}]", end=" <-> ")
            current = current.next
        print("None")

    #Show all values from end to start
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        #Go to the last node
        while current.next:
            current = current.next

        print("Backward: ", end="")
        while current:
            print(f"[{current.value}]", end=" <-> ")
            current = current.prev
        print("None")

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
