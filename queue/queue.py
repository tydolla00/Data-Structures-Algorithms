# This is a py file for queue

from stack.stack import Stack


class Queue(Stack):
    def __init__(self) -> None:
        pass
    
    def enqueue(val):
        """Push next in line into the Queue."""
        super().push(val)
        
    def dequeue(self):
        """Remove next in line from the Queue
        Returns:
            Type of element in queue.
        """
        return self.arr.pop(0)
    
    def rear():
        return super().top()
        
    def front(self):
        return self.arr[0]
    
    def contains(self, val):
        return self.arr.__contains__(val)

# Implement LinkedList Based Queue.

