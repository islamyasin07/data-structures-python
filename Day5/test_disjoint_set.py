from disjoint_set import DisjointSet

if __name__ == "__main__":
    ds = DisjointSet(7)  

    print("Initial state:")
    ds.display()

    print("\nPerforming unions...")
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)
    ds.union(5, 6)

    ds.display()

    print("\nCheck connections:")
    print("Are 0 and 2 connected?", ds.connected(0, 2))  # True
    print("Are 3 and 5 connected?", ds.connected(3, 5))  # False

    print("\nUnion 4 and 5...")
    ds.union(4, 5)
    ds.display()

    print("Are 3 and 6 connected?", ds.connected(3, 6))  # True
