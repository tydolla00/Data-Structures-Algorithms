// Bubble Sort, Merge Sort, Bucket Sort, Selection
class Sorting {
  public arr: number[];
  constructor(public array: number[]) {
    this.arr = array;
  }

  mergeSort(start: number, end: number) {
    if (end - start + 1 <= 1) return;
    const middle = (start + end) / 2;
    this.mergeSort(start, middle);
    this.mergeSort(middle + 1, end);
    this.merge(start, middle, end, this.arr);
  }

  private merge(start: number, middle: number, end: number, arr: number[]) {
    const L = arr.slice(start, middle);
    const R = arr.slice(middle, end);

    let i = 0,
      j = 0,
      k = 0;

    while (i < L.length && j < R.length) {
      if (L[i] <= R[j]) {
        arr[k] = L[i];
        i += 1;
      } else {
        arr[k] = R[j];
        j += 1;
      }
      k += 1;
    }
    while (i < L.length) {
      arr[k] = L[i];
      i += 1;
      k += 1;
    }
    while (j < R.length) {
      arr[k] = R[j];
      j += 1;
      k += 1;
    }
  }

  selectionSort() {
    for (let i = 0; i < this.arr.length; i++) {
      let j = i + 1;
      while (j < this.arr.length) {
        if (this.arr[i] > this.arr[j]) this.swap(i, j);
        j += 1;
      }
    }
  }

  bubbleSort() {
    let left = 0,
      right = this.arr.length - 1;
    while (left < right) {
      while (left + 1 < this.arr.length && left < right) {
        if (this.arr[left] > this.arr[left + 1]) this.swap(left, left + 1);
        left += 1;
      }
      left = 0;
      right -= 1;
    }
  }

  quickSort(start: number, right: number) { // Needs to be fixed.
    if (right - start - 1 <= 1) {
      return this.arr;
    }

    const pivotIndex = Math.floor((start + right) / 2);
    const pivot = this.arr[pivotIndex];
    let left = start;

    for (let i = left; i < right; i++) {
      if (this.arr[i] < pivot) {
        this.swap(left, i);
        left++;
      }
    }

    this.quickSort(start, pivotIndex);
    this.quickSort(pivotIndex + 1, right);
  }
  swap(val1: number, val2: number) {
    const temp = this.arr[val1];
    this.arr[val1] = this.arr[val2];
    this.arr[val2] = temp;
  }
}

const sort = new Sorting([100, 10, 8, 5, 2, 3, 4]);
sort.quickSort(0, sort.arr.length - 1);
console.log(sort.arr);
