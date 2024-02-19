class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_new_head(self, node):
        tempNode = self.head
        self.head = node
        node.next = tempNode
        tempNode.prev = node
    
    def insert_new_tail(self, node):
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    
    def insert(self, prevNode, node):
        tempNode = prevNode.next
        prevNode.next = node
        if tempNode:
            tempNode.prev = node
        else:
            self.tail = node
            self.tail.prev = prevNode
        node.prev = prevNode
        node.next = tempNode
    
    def delete(self, node):
        if self.head == node:
            if node.next == self.tail: 
                print("Cannot delete Head or Tail without other nodes.")
                return
            self.head = node.next
            return
        
        curr = self.head
        while curr.next != node and curr.next is not None:
            curr = curr.next
            
        if curr.next == node:
            if curr.next.next is None:
                self.tail = curr
                self.tail.next = None
                return
            curr.next.next.prev = curr
            curr.next = curr.next.next
                
    
    def print_list(self):
        node = self.head
        while node:
            print(f"Node [{node.val}] -> ", end="")
            node = node.next
        print("None")
    
    def search(self, val):
        curr = self.head
        while curr.val != val and curr.next is not None:
            curr = curr.next
        if curr.val == val:
            return True
        return False
    
    
class Node:
    def __init__(self, val=0) -> None:
        self.val = val
        self.prev = None
        self.next = None
        
linkedList = DoublyLinkedList()
linkedList.insert(linkedList.head, Node(1))
linkedList.insert_new_head(Node(69))
linkedList.insert_new_tail(Node(20))
linkedList.print_list() # 69 -> 0 -> 1 -> 0 -> 20 -> None
linkedList.delete(linkedList.head.next.next)
linkedList.print_list() # 69 -> 0 -> 0 -> 20 -> None
linkedList.delete(linkedList.tail) 
linkedList.print_list() # 69 -> 0 -> 0 -> None
linkedList.delete(linkedList.head)
linkedList.print_list() # 0 -> 0 -> None
linkedList.insert(linkedList.head, Node(100))
linkedList.delete(linkedList.head) 
linkedList.print_list() # 100 -> 0 -> None
print(linkedList.search(100)) # true