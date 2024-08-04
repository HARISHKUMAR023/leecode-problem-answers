class MyStack:

    def __init__(self):
        # Initialize the stack as an empty list
        self.myStack = []

    def push(self, x: int) -> None:
        # Append element to the stack
        self.myStack.append(x)

    def pop(self) -> int:
        # Pop the top element from the stack and return it
        return self.myStack.pop()

    def top(self) -> int:
        # Return the top element without removing it
        return self.myStack[-1]

    def empty(self) -> bool:
        # Check if the stack is empty
        return len(self.myStack) == 0

# Example usage:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# param_2 = obj.pop()  # Should return 2
# param_3 = obj.top()  # Should return 1
# param_4 = obj.empty() # Should return False
