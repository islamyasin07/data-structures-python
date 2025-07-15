from stack_linked_list import StackLinkedList

stack = StackLinkedList()

#Push some items
stack.push(100)
stack.push(200)
stack.push(300)

print("After pushing:")
stack.display()

print("Top item:", stack.invs())

print("Popped:", stack.pop())

print("After popping:")
stack.display()

print("Size:", stack.size())

#check if empty
print("Is empty?", stack.is_empty())
