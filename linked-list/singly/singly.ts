class SignlyLinkedList<T extends number> {
  head: LinkedListNode<T>;
  tail: LinkedListNode<T>;
  constructor() {
    this.head = new LinkedListNode<T>();
    this.tail = new LinkedListNode<T>();
    this.head.next = this.tail;
  }

  insertAtHead(node: LinkedListNode<T>) {
    const tempNode = this.head;
    this.head = node;
    node.next = tempNode;
  }

  insertNewTail(node: LinkedListNode<T>) {
    this.tail.next = node;
    this.tail = node;
  }

  insert(prevNode: LinkedListNode<T>, newNode: LinkedListNode<T>) {
    const tempNode = prevNode.next;
    prevNode.next = newNode;
    newNode.next = tempNode;
  }

  delete(node?: LinkedListNode<T>) {
    if (!node) {
      console.log("NaN, please pass in a Node.");
      return;
    }
    if (this.head == node) {
      if (node.next == this.tail) {
        console.log("Cannot delete Head or Tail without other nodes.");
        return;
      }
      this.head = <LinkedListNode<T>>node.next;
    }

    let prevNode = this.head;
    while (prevNode.next != node && prevNode.next) prevNode = prevNode.next;
    if (prevNode.next == node) {
      if (node == this.tail) {
        this.tail = prevNode;
      }
      prevNode.next = node.next;
    } else console.log("Node not found");
  }

  printList() {
    let node = this.head;
    let stringBuilder = "";
    while (node) {
      stringBuilder += `Node [${node.val}] -> `;
      node = <LinkedListNode<T>>node.next;
    }
    stringBuilder += "None";
    console.log(stringBuilder);
  }

  search(val: T) {
    let node = this.head;
    while (node.val !== val && node.next) node = node.next;
    node.val == val ? true : false;
  }
}

// class LinkedListNode<T extends number> {
//   next: LinkedListNode<T> | undefined = undefined;
//   constructor(public val?: T) {
//     this.val = val ? val : (0 as T);
//   }
// }

// const linkedList = new SignlyLinkedList<number>();
// linkedList.printList();
// linkedList.insert(linkedList.head, new LinkedListNode<number>(1));
// linkedList.insertAtHead(new LinkedListNode<number>(69));
// linkedList.printList(); // 69 -> 0 -> 1 -> 0
// linkedList.delete(linkedList.head.next?.next);
// linkedList.printList(); // 69 -> 0 -> 0 -> None
// linkedList.delete(linkedList.tail);
// linkedList.printList(); // 69 -> 0 -> None
// linkedList.delete(linkedList.head); // Error
// linkedList.printList();
// linkedList.insert(linkedList.head, new LinkedListNode<number>(100));
// linkedList.delete(linkedList.head);
// linkedList.printList(); // 100 -> 0 -> None
