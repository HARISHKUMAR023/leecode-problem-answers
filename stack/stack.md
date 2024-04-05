``` python
# createstack
def createstack():
    stack = []
    return stack

# checking if the stack is empty
def check_stackempty(stack):
    return len(stack) == 0 

# inserting an item into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)

# deleting an item from the stack    
def pop(stack):
    if check_stackempty(stack):
        return "stack is empty"
    return stack.pop()

# Main function
print("********************* Welcome to Stack Operations ****************** ")

while True:
    print("\nChoose an operation:")
    print("1. Insertion in stack")
    print("2. Deletion in stack")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    stack = createstack()

    if choice == 1:
        totalnum = int(input("Enter the total items to be inserted in the stack: "))
        for i in range(totalnum):
            num = input("Enter the number to be inserted: ")
            push(stack, str(num))
        print("Stack elements after insertion: " + str(stack))

    elif choice == 2:
        print("Popped item: " + pop(stack))
        print("The updated stack is: ", str(stack))

    elif choice == 0:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")

print("Thank you for using the stack operations. Happy coding!")
