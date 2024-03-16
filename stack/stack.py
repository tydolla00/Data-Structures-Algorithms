class Stack:
    def __init__(self) -> None:
        self.arr = []
    
    def push(self, obj):
        self.arr.append(obj)
    
    def pop(self):
        if not self.isEmpty():
            return self.arr.remove(self.arr[-1])
    
    def top(self):
        return self.arr[-1] if not self.is_empty() else "Stack is empty."
    
    def is_empty(self):
        return len(self.arr) <= 0
    
    def size(self):
        return len(self.arr)
    
    def printStack(self):
        print(self.arr)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.top())