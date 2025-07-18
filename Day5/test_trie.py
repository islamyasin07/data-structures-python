from trie import Trie

if __name__ == "__main__":
    trie = Trie()

    print("Inserting words into the trie...")
    trie.insert("cat")
    trie.insert("car")
    trie.insert("cart")
    trie.insert("dog")

    print("\nSearching for words:")
    print("Search 'car':", trie.search("car"))       # True
    print("Search 'cart':", trie.search("cart"))     # True
    print("Search 'can':", trie.search("can"))       # False

    print("\nChecking prefixes:")
    print("Starts with 'ca':", trie.starts_with("ca"))  # True
    print("Starts with 'do':", trie.starts_with("do"))  # True
    print("Starts with 'da':", trie.starts_with("da"))  # False
