# **Stack**
Stack is a data structure that operates in a First In First Out paradigm (FIFO). Items pushed last onto the stack are then removed first. It is one of the most fundamental data structures and is essential to understanding it's implementation.

So how does it work? Think of a stack as a collection (stack) of plates. When you put away plates after washing them you put them on top of the last one. When you want to take a plate from the stack you take from the top. That's how stack works. In it's most basic implementation, stack has a few methods.

### Methods
- **Push**: push onto the top of the stack a new item. Time Complexity O(1)
- **Pop**: remove a item from the top of the stack. Time Complexity O(1)
- **Peek**: view the top of the stack. Time ComplexityO(1)
- **IsEmpty**: return boolean if the instance of this stack is empty. Time Complexity O(1)
- **Size**: return the size of the stack, how many items are stored in the stack currently. Time Complexity O(1)

### Push
Each item is pushed onto the top allowing for ease of access and fast retrieval. Pushing item 2 after item 1, results in item 2 being in front of item 1 in the order of retrieval on the stack.

<img width="859" alt="image" src="https://github.com/tydolla00/Data-Structures-Algorithms/assets/90355178/cd27b5d0-a3d4-4a0b-8344-5dc9f9787661">

### Pop
The top of the stack is removed and items in the stack are shifted towards the top. 

<img width="709" alt="image" src="https://github.com/tydolla00/Data-Structures-Algorithms/assets/90355178/94504194-31fd-45fa-9d47-f90e8dea6f60">


# Applications/When to use a Stack
- *Function calls*: Stacks are used to keep track of the return address
- *History*: Stacks are used to keep track of state, such as a browsing history. Navigating to a page and clicking links you're always able to go backwards.

Stacks are useful when you don't care about accessing a random element and want fast retrieval.

# Advantages 
- *Performant*: Insertion and Deletion is O(1) making it an efficent DS.
- *Simplicity*: Stacks are easy to implement and even easier to understand.
- *Efficient Memory usage*: only need the space necessary for each current item in a stack. Space Complexity O(n)

# Disadvantages
- *Limited Access*: Can only retrieve last pushed item.


# Support
### Built in ✅ | Not Built In ❌
- **C#**: ✅  
- **Java**: ✅ 
- **Python**: ❌ 
- **TS**: ❌

# Resources
#### Think of how you can implement a stack in your own workflow. Check out an implementation in [Typescript](stack.ts) [Java](stack.java) [C#](stack.cs) [Python](stack.py)
[Geek for Geeks Stack](https://www.geeksforgeeks.org/stack-data-structure/?ref=lbp)