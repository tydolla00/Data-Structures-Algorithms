class Heap<T>{
    heap: T[]
    constructor(val: T){
        this.heap = [val]
    }

    push(val: T){
        this.heap.push(val)
        let i = this.heap.length - 1
        while (this.heap[i] < this.heap[i / 2]){
            const temp = this.heap[i]
            this.heap[i] = this.heap[i / 2]
            this.heap[i / 2] = temp
            i = i / 2
        }
    }

    pop(){
        if (this.heap.length == 1) return null
        if (this.heap.length == 2) return this.heap.pop()

        const res = this.heap[1]
        this.heap[1] = this.heap.pop() as T 
        const i = 1
        this.percolateDown(i)
        return res
    }

    percolateDown(i: number){
        while (2 * i < this.heap.length){
            if (
                2 * i + 1 < this.heap.length
                && this.heap[2 * i + 1] < this.heap[2 * i]
                && this.heap[i] > this.heap[2 * i + 1]
            ){
                const temp = this.heap[i]
                this.heap[i] = this.heap[2 * i + 1]
                this.heap[2 * i + 1] = temp
                i = 2 * i + 1
            } else if (this.heap[i] > this.heap[2 * i]){
                const temp = this.heap[i]
                this.heap[i] = this.heap[2 * i]
                this.heap[2 * i] = temp
                i = 2 * i
            } else break
        }
    }
}