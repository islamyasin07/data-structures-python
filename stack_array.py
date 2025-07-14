class StackArray:
    def __init__(self):
        #Create an empty list
        self.stack = []

    #Add a new item to the top of the stack
    def push(self, value):
        self.stack.append(value)

    #Remove item from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")

    #View the top item without removing it
    def invs(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Empty stack")

    #Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    #return the number of items in the stack
    def size(self):
        return len(self.stack)

    #Print the stack contents from end to top
    def display(self):
        print("Stack:", self.stack)
