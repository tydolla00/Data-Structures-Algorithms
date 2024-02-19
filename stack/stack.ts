class Stack<T>{
    private arr: T[]
    constructor(){
        this.arr = []
    }
    push(newVal: T){
        this.arr.push(newVal)
    }
    pop(){
        this.arr.pop()
    }
    top(){
        return this.arr[-1]
    }
    isEmpty(){
        return this.arr.length == 0
    }
    size(){
        return this.arr.length
    }
    
    printStack(){
        console.log(this.arr)
    }
}

const stack = new Stack<number>()
