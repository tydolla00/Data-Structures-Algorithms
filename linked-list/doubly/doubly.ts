class DoublyLinkedList<T extends number> {
  head: LinkedListNode<T>;
  tail: LinkedListNode<T>;
  constructor() {
    this.head = new LinkedListNode();
    this.tail = new LinkedListNode();
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  insertAtHead(node: LinkedListNode<T>) {
    const tempNode = this.head;
    this.head = node;
    node.next = tempNode;
    tempNode.prev = node;
  }

  insertAtTail(node: LinkedListNode<T>) {
    this.tail.next = node;
    node.prev = this.tail;
    this.tail = node;
  }

  insert(prevNode: LinkedListNode<T>, node: LinkedListNode<T>) {
    const tempNode = prevNode.next;
    prevNode.next = node;
    if (tempNode) tempNode.prev = node;
    else {
      this.tail = node;
      this.tail.prev = prevNode;
    }
    node.prev = prevNode;
    node.next = tempNode;
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
      this.head = this.head.next!;
      return;
    }

    let curr = this.head;
    while (curr.next != node && curr.next) curr = curr.next;
    if (curr.next == node) {
      if (curr.next.next == undefined) {
        this.tail = curr;
        this.tail.next = undefined;
        return;
      }
      curr.next.next.prev = curr;
      curr.next = curr.next.next;
    }
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
    return node.val == val ? true : false;
  }
}

class LinkedListNode<T extends number> {
  next: LinkedListNode<T> | undefined = undefined;
  prev: LinkedListNode<T> | undefined = undefined;
  constructor(public val?: T) {
    this.val = val ? val : (0 as T);
  }
}

const linkedList = new DoublyLinkedList();
linkedList.insert(linkedList.head, new LinkedListNode<number>(1));
linkedList.insertAtHead(new LinkedListNode<number>(69));
linkedList.insertAtTail(new LinkedListNode<number>(20));
linkedList.printList(); // 69 -> 0 -> 1 -> 0 -> 20 -> None
linkedList.delete(linkedList.head?.next?.next);
linkedList.printList(); // 69 -> 0 -> 0 -> 20 -> None
linkedList.delete(linkedList.tail);
linkedList.printList(); // 69 -> 0 -> 0 -> None
linkedList.delete(linkedList.head);
linkedList.printList(); // 0 -> 0 -> None
linkedList.insert(linkedList.head, new LinkedListNode<number>(100));
linkedList.delete(linkedList.head);
linkedList.printList(); // 100 -> 0 -> None
console.log(linkedList.search(100)); // true
