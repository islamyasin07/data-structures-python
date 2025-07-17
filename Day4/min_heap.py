class MinHeap:
    def __init__(self):
        self.heap = []  
    #Get index of parent
    def parent(self, i):
        return (i - 1) // 2

    #Get index of left child
    def left(self, i):
        return 2 * i + 1

    #Get index of right child
    def right(self, i):
        return 2 * i + 2

    # Swap two values in the heap
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Insert a new number into the heap
    def insert(self, value):
        self.heap.append(value)  
        self._heapify_up(len(self.heap) - 1)  

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def remove_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]  # root value
        self.heap[0] = self.heap.pop()  # move last to root
        self._heapify_down(0)  # fix the heap
        return min_value

    def _heapify_down(self, index):
        smallest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self._heapify_down(smallest)

    def display(self):
        print("Min Heap:", self.heap)
