from doubly_linked_list import DoublyLinkedList

smp = DoublyLinkedList()

smp.append(10)
smp.append(20)
smp.append(30)
print("After append:")
smp.display_forward()

smp.display_backward()

smp.prepend(5)
smp.prepend(1)

print("After prepend:")
smp.display_forward()
smp.display_backward()

smp.remove(20)
print("After removing 20:")
smp.display_forward()

smp.remove(100)

print("List size:", smp.size())
