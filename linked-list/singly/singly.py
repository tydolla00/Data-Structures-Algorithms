class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        
    def insert_new_head(self, node):
        tempNode = self.head
        self.head = node
        node.next = tempNode
        
    def insert_new_tail(self,node):
        self.tail.next = node
        self.tail = node
        
    def insert(self, prevNode, newNode):
        tempNode = prevNode.next
        prevNode.next = newNode
        newNode.next = tempNode
        
    def delete(self, node):
        if self.head == node:
            if node.next == self.tail: 
                print("Cannot delete Head or Tail without other nodes.")
                return
            self.head = node.next
            return
        
        prevNode = self.head
        while prevNode.next != node and prevNode.next is not None:
            prevNode = prevNode.next
        if prevNode.next == node:
            if node == self.tail:
                self.tail = prevNode
            prevNode.next = node.next
        else:
            print("Node not found")
        
    def printList(self):
        node = self.head
        while node:
            print(f"Node [{node.val}] -> ", end="")
            node = node.next
        print("None")
    
    def search(self, val):
        node = self.head
        while node.val != val and node.next is not None:
            node = node.next
        if node.val == val:
            return True
        return False
            
class Node:
    def __init__(self, val=0) -> None:
        self.val = val
        self.next = None
        
linkedList = SinglyLinkedList()
linkedList.delete(linkedList.head)
linkedList.insert(linkedList.head, Node(1))
linkedList.insert_new_head(Node(69))
linkedList.insert_new_tail(Node(20))
linkedList.printList()
linkedList.delete(linkedList.head.next.next)
linkedList.printList() # 69 -> 0 -> 0 -> None
linkedList.delete(linkedList.tail) 
linkedList.printList() # 69 -> 0 -> None
linkedList.delete(linkedList.head) # Error
linkedList.printList()  
linkedList.insert(linkedList.head, Node(100))
linkedList.delete(linkedList.head) 
linkedList.printList() # 100 -> 0 -> None
print(linkedList.search(100))