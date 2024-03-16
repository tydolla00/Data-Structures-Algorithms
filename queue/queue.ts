type NumOrString = number | string;
class Stack<T extends NumOrString> {
  arr: T[];
  constructor() {
    this.arr = [];
  }
  protected push(newVal: T) {
    this.arr.push(newVal);
  }
  protected pop() {
    return this.arr.pop();
  }
  protected top() {
    return this.arr[this.arr.length - 1];
  }
  isEmpty() {
    return this.arr.length == 0;
  }
  size() {
    return this.arr.length;
  }

  printStack() {
    console.log(this.arr);
  }
}

class Queue<T extends NumOrString> extends Stack<T> {
  enqueue(val: T) {
    super.push(val);
  }
  dequeue() {
    return this.arr.shift();
  }
  rear() {
    return this.top();
  }
  front() {
    return this.arr[0];
  }
  contains(val: T) {
    return this.arr.includes(val);
  }
}
// Queue goes right to left. Left first to go
const queue = new Queue<number>();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);
queue.enqueue(4);
queue.enqueue(5);
queue.enqueue(6);
queue.dequeue();
console.log(queue.front()); // 2
console.log(queue.rear()); // 6
console.log(queue.printStack()); // 2 -> 3 -> 4 -> 5 -> 6
