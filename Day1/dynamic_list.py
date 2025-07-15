class DynamicList:
    # Initialize the dynamic list
    def __init__(self):
        self.data = []

    # Add an element to the end of the list
    def add(self, value):
        self.data.append(value)

    # Insert an element at a specific index
    def insert_at(self, index, value):
        if 0 <= index <= len(self.data):
            self.data.insert(index, value)
        else:
            raise IndexError("Invalid index for insertion")

    # Remove an element by its value
    def remove(self, value):
        if value in self.data:
            self.data.remove(value)
        else:
            raise ValueError("Value not found in the list")

    # Return the size of the list
    def size(self):
        return len(self.data)

    # Return the element at the specified index
    def get_at(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Invalid index")

    # String representation of the dynamic list
    def __str__(self):
        return str(self.data)
