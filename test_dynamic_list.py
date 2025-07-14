from dynamic_list import DynamicList
#Object to test the DynamicList class
my_list = DynamicList()

#Adding elements to the list
my_list.add(10)
my_list.add(20)
my_list.add(30)
print("After add:", my_list)

#inserting at a specific index
my_list.insert_at(1, 15)
print("After insert at index 1:", my_list)

#Removal Test
my_list.remove(20)
print("After removing 20:", my_list)

#Size method test
print("Size of list:", my_list.size())


print("Element at index 0:", my_list.get_at(0))
