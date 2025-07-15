class QueueArray:
    def __init__(self):
        #Create an empty list 
        self.queue = []

    #Add an item to the end of the queue
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeueing failed - Empty Queue")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Front from empty queue")

    #Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", self.queue)
