from min_heap import MinHeap

if __name__ == "__main__":
    heap = MinHeap()

    print("Inserting numbers into the heap...")
    heap.insert(40)
    heap.insert(20)
    heap.insert(60)
    heap.insert(10)
    heap.insert(30)

    print("\nHeap after insertions:")
    heap.display()

    print("\nRemoving the smallest number...")
    print("Removed:", heap.remove_min())

    print("\nHeap after removing min:")
    heap.display()

    print("\nInserting more numbers...")
    heap.insert(5)
    heap.insert(25)

    print("\nFinal heap:")
    heap.display()
