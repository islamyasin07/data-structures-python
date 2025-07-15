from queue_array import QueueArray

queue = QueueArray()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("After enqueue:")
queue.display()  

print("Front item:", queue.front())  


removed = queue.dequeue()
print("Dequeued item:", removed)  #Output: 10


print("After dequeue:")
queue.display()  #Output:[20, 30]

print("Queue size:", queue.size()) 

print("Is it empty?", queue.is_empty())  #Output: False
