from circular_linked_list import CircularLinkedList

smp = CircularLinkedList()

smp.append("A")
smp.append("B")
smp.append("C")

print("After append:")
smp.display()

print("List size:", smp.size())

smp.remove("B")
print("After removing B:")
smp.display()

smp.remove("X")  

smp.remove("A")
print("After removing A (head):")
smp.display()


smp.remove("C")
print("After removing all:")
smp.display()

print("Final size:", smp.size())
