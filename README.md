# Data Structures in Python – OppoTrain Intensive Week

This repository contains Python implementations of core data structures as part of the **OppoTrain Summer 2025 Practical Training Week**.  
All structures are implemented from scratch with clear documentation and basic usage examples.

---

## 📅 Day 1 Tasks

| Data Structure              | Status | File Name                     |
|----------------------------|--------|-------------------------------|
| Dynamic Array              | ✅ Done | `Day1/dynamic_list.py`        |
| Singly Linked List         | ✅ Done | `Day1/singly_linked_list.py`  |
| Stack (using array)        | ✅ Done | `Day1/stack_array.py`         |
| Stack (using linked list)  | ✅ Done | `Day1/stack_linked_list.py`   |

---
## 📅 Day 2 Tasks

| Data Structure              | Status | File Name                          |
|----------------------------|--------|-------------------------------------|
| Queue (using linked list)  | ✅ Done | `Day2/queue_linked_list.py`         |
| Doubly Linked List         | ✅ Done | `Day2/doubly_linked_list.py`        |
| Circular Linked List       | ✅ Done | `Day2/circular_linked_list.py`      |

---



## 📁 Folder Structure (Day1)

```
Day1/ 
├── dynamic_list.py
├── singly_linked_list.py
├── stack_array.py
├── stack_linked_list.py
├── test_dynamic_list.py
├── test_singly_linked_list.py
├── test_stack_array.py
├── test_stack_linked_list.py
``` 


## ⚙️ How to Run (Day 1)
You can run any file using Python :
`Day1/test_stack_linked_list.py` 


## ⚙️ How to Run (Day 2)
You can run any file using Python :
 `Day2/test_queue_linked_list.py`
 `Day2/test_doubly_linked_list.py`
 `Day2/test_circular_linked_list.py`



## 📌 Description of Each Data Structure (Day 1)

- **DynamicList**
  - Uses built-in Python `list`
  - Methods: `add`, `insert_at`, `remove`, `get_at`, `size`
  - File: `dynamic_list.py`

- **SinglyLinkedList**
  - Node-based linked list structure
  - Methods: `add`, `remove`, `display`, `size`, `get_at`
  - File: `singly_linked_list.py`

- **StackArray**
  - Stack implemented using Python `list` (LIFO)
  - Methods: `push`, `pop`, `invs`, `is_empty`, `size`, `display`
  - File: `stack_array.py`

- **StackLinkedList**
  - Stack using a custom linked list structure
  - Methods: `push`, `pop`, `invs`, `is_empty`, `size`, `display`
  - File: `stack_linked_list.py`


## 📌 Description of Each Data Structure (Day 2)

- **Queue (Linked List)**
  - Uses built-in Python `list`
  - Methods: `enqueue`, `dequeue`, `display`, `size`, `invs`
  - File: `queue_linked_list.py`

- **Doubly Linked List**
  - Each node has next and prev
  - Methods: `append`, `prepend`, `remove`, `display_forward`, `display_backward`
  - File: `doubly_linked_list.py`

- **Circular Linked List**
  - Last node connects back to head
  - Methods: `append`, `remove`, `display`, `size`, 
  - File: `circular_linked_list.py`



