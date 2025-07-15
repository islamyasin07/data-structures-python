class Node:
    def __init__(self, value):
        self.value = value
        self.next = self


class CircularLinkedList:
    def __init__(self):
        self.head = None

    #Add a node at the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            #Go to the last node
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    #Remove a node by value
    def remove(self, value):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        prev = None

        while True:
            if current.value == value:
                if prev is None:
                    if current.next == self.head:
                        self.head = None
                    else:
                        tail = self.head
                        while tail.next != self.head:
                            tail = tail.next
                        tail.next = current.next
                        self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            if current == self.head:
                break

        print("Value not found")

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        print("Circular List:", end=" ")
        while True:
            print(f"[{current.value}]", end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(f"({current.value} back to head)")

    def size(self):
        if self.head is None:
            return 0
        count = 1
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next
        return count
