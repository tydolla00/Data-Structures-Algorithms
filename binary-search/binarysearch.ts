const binarySearch = <T> (arr: T[], query: T) => {
    let left=0,right=arr.length - 1

    while (left <= right){
        const mid = (left + right) / 2 

        if (query > arr[mid]) left = mid + 1
        else if (query < arr[mid]) right = mid - 1
        else return mid
    }
    return -1
}

const arr = [1,2,3,4,5]
console.log(binarySearch(arr, 100))