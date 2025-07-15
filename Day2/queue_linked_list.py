class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    #Add an item to the end of the queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    #Remove the front item
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        removed_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_value

    def invs(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value

    #Return number of elements in the queue
    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    #Check if the queue is empty
    def is_empty(self):
        return self.front is None

    #Print all values from front to rear
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        print("Queue (front → rear): ", end="")
        while current:
            print(f"[{current.value}]", end=" -> ")
            current = current.next
        print("None")

    def enqueue_from_input(self):
        try:
            count = int(input("How many items do you want to add? "))
            for _ in range(count):
                val = input("Enter value: ")
                self.enqueue(val)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
