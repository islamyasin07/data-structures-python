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
| Queue (Array)              | ✅ Done | `Day2/doubly_linked_list.py`        |

---
## 📅 Day 3 Tasks

| Data Structure              | Status   | File Name                            |
|----------------------------|----------|---------------------------------------|
| Binary Tree                | ✅ Done  | `Day3/binary_tree.py`                |
| Binary Search Tree (BST)   | ✅ Done  | `Day3/binary_search_tree.py`         |
| Tree Traversals            | ✅ Done  | Included in both tree files above    |
| STAR Behavioral Questions  | ✅ Done  | See: `Day3/README.md`                |

---
📌 **Note:**  
Day 3 includes a separate `README.md` inside the `Day3/` folder which contains:

- ✅ STAR responses for 5+ behavioral interview questions  
- ✅ Screenshots of AI feedback  
- ✅ Summary of mock interview practice via Exponent  
---

## 📅 Day 4 Tasks

| Data Structure             | Status   | File Name                            |
|----------------------------|----------|---------------------------------------|
| Hash Table (with chaining) | ✅ Done  | `Day4/hash_table.py`                 |
| Min Heap                   | ✅ Done  | `Day4/min_heap.py`                   |
| Graph (Adjacency List)     | ✅ Done  | `Day4/graph.py`                      |
| Visualizations & Screenshots | ✅ Done  | See: `Day4/graph_visual.py`, `hash_table_visual.py`, `images/` |

---
📌 **Note:**  
Day 4 includes a separate `README.md` inside the `Day4/` folder which contains: Visualizations & Screenshots for graph & hash table

---
## 📅 Day 5 Tasks

| Data Structure              | Status   | File Name                             |
|-----------------------------|----------|----------------------------------------|
| Trie                        | ✅ Done  | `Day5/trie.py`                         |
| Union-Find (Disjoint Set)   | ✅ Done  | `Day5/disjoint_set.py`                |
| Graph Traversal (BFS & DFS) | ✅ Done  | `Day5/graph_traversal.py`             |
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

## 📁 Folder Structure (Day2)

```
Day2/ 
├── queue_array.py
├── doubly_linked_list.py
├── circular_linked_list.py
├── queue_linked_list.py
├── test_queue_linked_list.py
├── test_doubly_linked_list.py
├── test_circular_linked_list.py
├── test_queue_array.py
``` 

## 📁 Folder Structure (Day3)

```
Day3/
├── binary_tree.py
├── binary_search_tree.py
├── test_binary_tree.py
├── test_binary_search_tree.py
├── README.md ← (STAR responses & feedback screenshots)
├── images/
│ ├── manage_conflict_question.png
│ └── prioritize_tasks_question.png
```

## 📁 Folder Structure (Day4)

```
Day4/
├── hash_table.py
├── min_heap.py
├── graph.py
├── test_hash_table.py
├── test_min_heap.py
├── test_graph.py
```
## 📁 Folder Structure (Day5)

```
Day5/
├── trie.py
├── disjoint_set.py
├── graph_traversal.py
├── test_trie.py
├── test_disjoint_set.py
├── test_graph_traversal.py
```

## ⚙️ How to Run (Day 1)
You can run any file using Python :
`Day1/test_stack_linked_list.py` 

## ⚙️ How to Run (Day 2)
You can run any file using Python :
 `Day2/test_queue_linked_list.py`
 `Day2/test_doubly_linked_list.py`
 `Day2/test_circular_linked_list.py`
 `Day2/test_queue_array.py`

## ⚙️ How to Run (Day 3)
Use `py` to run each test file manually:
 `Day3/test_binary_tree.py`
 `Day3/test_binary_search_tree.py`

## ⚙️ How to Run (Day 4)
Use `py` to run each test file manually:
 `Day4/test_graph.py`
 `Day4/test_hash_table.py`
 `Day4/test_min_heap.py`

## ⚙️ How to Run (Day 5)

Use `py` to run each test file manually:

`py Day5/test_trie.py`  
`py Day5/test_disjoint_set.py`  
`py Day5/test_graph_traversal.py`



## 📌 Description of Each Data Structure (Day 1)

- **DynamicList**
  - Uses built-in Python `list`
  - Methods: `add`, `insert_at`, `remove`, `get_at`, `size`
  - File: `dynamic_list.py`
  - **Time Complexity:** O(1) for append, O(n) for insert/remove
  - **Space Complexity:** O(n)

- **SinglyLinkedList**
  - Node-based linked list structure
  - Methods: `add`, `remove`, `display`, `size`, `get_at`
  - File: `singly_linked_list.py`
  - **Time Complexity:** O(1) insert at head, O(n) search/remove
  - **Space Complexity:** O(n)

- **StackArray**
  - Stack implemented using Python `list` (LIFO)
  - Methods: `push`, `pop`, `invs`, `is_empty`, `size`, `display`
  - File: `stack_array.py`
  - **Time Complexity:** O(1) for push/pop
  - **Space Complexity:** O(n)

- **StackLinkedList**
  - Stack using a custom linked list structure
  - Methods: `push`, `pop`, `invs`, `is_empty`, `size`, `display`
  - File: `stack_linked_list.py`
  - **Time Complexity:** O(1) for push/pop
  - **Space Complexity:** O(n)

## 📌 Description of Each Data Structure (Day 2)

- **Queue (Linked List)**
  - Uses custom linked list
  - Methods: `enqueue`, `dequeue`, `display`, `size`, `invs`
  - File: `queue_linked_list.py`
  - **Time Complexity:** O(1) for enqueue/dequeue
  - **Space Complexity:** O(n)

- **Doubly Linked List**
  - Each node has next and prev
  - Methods: `append`, `prepend`, `remove`, `display_forward`, `display_backward`
  - File: `doubly_linked_list.py`
  - **Time Complexity:** O(1) insert at head/tail, O(n) search/remove
  - **Space Complexity:** O(n)

- **Circular Linked List**
  - Last node connects back to head
  - Methods: `append`, `remove`, `display`, `size`
  - File: `circular_linked_list.py`
  - **Time Complexity:** O(1) insert at tail (if tail saved), O(n) remove
  - **Space Complexity:** O(n)

## 📌 Description of Each Data Structure (Day 3)

- **Binary Tree**
  - Traversals: inorder, preorder, postorder
  - File: `binary_tree.py`
  - **Time Complexity:** O(n) for traversals
  - **Space Complexity:** O(h) where h = tree height (recursion stack)

- **Binary Search Tree (BST)**
  - Automatically places elements based on value
  - Methods: insert, search, inorder, preorder, postorder
  - File: `binary_search_tree.py`
  - **Time Complexity:** O(log n) average, O(n) worst-case
  - **Space Complexity:** O(n)

## 📌 Description of Each Data Structure (Day 4)

- **HashTable**
  - Stores key-value pairs using list of buckets (chaining)
  - Methods: `insert`, `get`, `remove`, `display`
  - File: `hash_table.py`
  - **Time Complexity:** O(1) average, O(n) worst (collisions)
  - **Space Complexity:** O(n)

- **MinHeap**
  - Keeps smallest value at the top using list-based binary heap
  - Methods: `insert`, `remove_min`, `display`
  - File: `min_heap.py`
  - **Time Complexity:** O(log n)
  - **Space Complexity:** O(n)

- **Graph**
  - Directed graph using adjacency list (dictionary of neighbors)
  - Methods: `add_vertex`, `add_edge`, `display`
  - File: `graph.py`
  - **Time Complexity:** O(1) for add, O(n) for display
  - **Space Complexity:** O(V + E)

## 📌 Description of Each Data Structure (Day 5)

- **Trie**
  - Tree-like structure used for fast word/prefix lookup
  - Methods: `insert`, `search`, `starts_with`
  - File: `trie.py`
  - **Time Complexity:** O(m) where m = length of word
  - **Space Complexity:** O(n * a) where n = number of words, a = alphabet size

- **Disjoint Set (Union-Find)**
  - Tracks connected components efficiently
  - Methods: `find`, `union`, `connected`, `display`
  - File: `disjoint_set.py`
  - **Time Complexity:** O(α(n)) 
  - **Space Complexity:** O(n)

- **Graph Traversal**
  - Represents a directed graph using an adjacency list
  - File: `graph_traversal.py`
  - **Time Complexity:** O(V + E)
  - **Space Complexity:** O(V)







