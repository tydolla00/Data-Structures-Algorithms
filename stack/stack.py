class Stack:
    def __init__(self) -> None:
        self.arr = []
    
    def push(self, obj):
        self.arr.append(obj)
    
    def pop(self):
        if not self.isEmpty():
            self.arr.remove(self.arr[-1])
    
    def top(self):
        return self.arr[-1] if not self.isEmpty() else "Stack is empty."
    
    def isEmpty(self):
        return len(self.arr) <= 0
    
    def size(self):
        return len(self.arr)
    
    def printStack(self):
        print(self.arr)
    
stack = Stack()
stack.top()