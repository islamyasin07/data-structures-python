from hash_table import HashTable

if __name__ == "__main__":
    ht = HashTable()

    print("Inserting student grades...")
    ht.insert("Ali", 75)
    ht.insert("Sara", 88)
    ht.insert("Omar", 92)
    ht.insert("Lana", 80)

    print("\nHash Table content:")
    ht.display()

    print("\nGetting grade for 'Sara':")
    print(ht.get("Sara"))  

    print("\nUpdating 'Sara' grade to 90...")
    ht.insert("Sara", 90)
    print("Updated grade:", ht.get("Sara")) 

    print("\nRemoving 'Ali' from the table...")
    ht.remove("Ali")
    print("After removal:")
    ht.display()

    print("\nTrying to get grade for a student not in the table - (Ziad):")
    print(ht.get("Ziad"))  
