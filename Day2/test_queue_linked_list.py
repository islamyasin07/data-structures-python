from queue_linked_list import QueueLinkedList
queue = QueueLinkedList()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("After enqueue:")
queue.display()

try:
    print("Front item:", queue.invs())
except IndexError as e:
    print(e)

try:
    removed = queue.dequeue()
    print("Dequeued:", removed)
except IndexError as e:
    print(e)

print("After a dequeue:")
queue.display()

print("Queue size:", queue.size())

print("Is it empty?", queue.is_empty())

try:
    queue.dequeue()
    queue.dequeue()
    print("After removing all:")
    queue.display()
except IndexError as e:
    print(e)
print("Final empty check:", queue.is_empty())
