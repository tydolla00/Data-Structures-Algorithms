from collections import deque

class Node:
    def __init__(self, val = None) -> None:
        self.left = None
        self.right = None
        self.val = val
        
class Binary_Tree:
    def __init__(self, val) -> None:
        self.root = Node(val)
    
    def insert(self,root: Node,val) -> Node: # O(logn)
        if not root:
            return Node(val)
        
        if val > root.right:
            root.right = self.insert(root.right, val)
        elif val < root.right:
            root.left = self.insert(root.left, val)
        return root
    
    def delete(self, root: Node, val) -> Node | None: # O(logn)
        if not root:
            return None
        
        if val > root.val:
            root.right = self.delete(root.right,val)
        elif val < root.val:
            root.left = self.delete(root.left,val)
        else:
            if not root.left:
                return root.right
            elif not root.right: 
                return root.left
            else:
                minNode = self.min_val(root.right)
                root.val = minNode.val
                root.right = self.delete(root.right, minNode.val)
    
    def search(self, root: Node, val) -> Node | None: # O(logn)
        if root is None:
            return None
        
        if val > root.val: 
            self.search(self,root.right,val)
        elif val < root.val:
            self.search(self, root.left, val)
        else: 
            return root
        
    def min_val(self, root) -> Node: # O(logn)
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr
    
    def inorder(self,root: Node): # O(n)
        if root is None: 
            return 
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)
        
    def preorder(self,root: Node): # O(n)
        if root is None: 
            return 
        print(root.val)
        self.inorder(root.left)
        self.inorder(root.right)
        
    def postoder(self,root: Node): # O(n)
        if root is None: 
            return 
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.val)
        
    def bfs(self, root: Node): # O(n)
        queue = deque()
        
        if root:
            queue.append(root)
            
        level = 0
        while len(queue) > 0:
            print("Level :", level)
            for i in range(len(queue)):
                curr = queue.popleft()
                print(curr)
                if curr.left:
                    queue.append(curr.left) 
                if curr.right:
                    queue.append(curr.right)
            level += 1