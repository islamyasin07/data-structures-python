from stack_array import StackArray
stack = StackArray()

stack.push(5)
stack.push(10)
stack.push(15)
print("After pushing 3 items:")
stack.display()
print("Top item => :", stack.invs())

popped = stack.pop()
print("Popped item:", popped)

print("After popping :")
stack.display()

print("Stack size:", stack.size())

print("Is it empty?", stack.is_empty())

while not stack.is_empty():
	stack.pop()

print("After popping all items:")
print("Is it empty now?", stack.is_empty())
