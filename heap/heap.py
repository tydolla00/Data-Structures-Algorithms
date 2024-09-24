class Heap:
    def __init__(self) -> None:
        self.heap = [0]

    def push(self, val: int):
        """
        Pushes a new element into the heap. Then percolates up to find it's correct position. O(logn)
        Args:
            val (int): _description_
        """
        self.heap.append(val)
        i = len(self.heap) - 1
        while self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def pop(self) -> int:
        """
        Removes the min element and recalculates the heap. O(logn)
        Returns:
            int: The top of the heap aka the minimum value.
        """
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        self.percolate_down(i)
        return res

    def heapify(self, arr): 
        """
        Convert an array into a min heap. O(n)
        """
        arr.append(arr[0])
        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            i = cur
            self.percolate_down(i)
            cur -= 1

    def percolate_down(self, i: int):
        """
        Checks an element and compares it against its' left and right children.
        If it is greater than either child, swap it.
        Args:
            i (int): index of element of which to check children.
        """
        while 2 * i < len(self.heap):
            if (
                2 * i + 1 < len(self.heap)
                and self.heap[2 * i + 1] < self.heap[2 * i]
                and self.heap[i] > self.heap[2 * i + 1]
            ):
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                break


newHeap = Heap()
