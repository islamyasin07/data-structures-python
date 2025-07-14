from singly_linked_list import SinglyLinkedList

my_list = SinglyLinkedList()
my_list.add(10)
my_list.add(20)
my_list.add(30)
print("After adding elements:")
my_list.display()

my_list.remove(20)
print("After removing 20:")
my_list.display()

print("Size:", my_list.size())
print("Element at 1:", my_list.get_at(1))
