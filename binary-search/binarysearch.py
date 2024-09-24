# from ast import List

def binarySearch(arr,num):
    left,right = 0, len(arr) -1
    while left <= right:
        mid =( left + right ) // 2
        if num > arr[mid]:
            left = mid + 1
        elif num < arr[mid]:
            right = mid - 1
        else: 
            return mid
    return -1

arr = [1,2,3,4,5]
# print(binarySearch(arr, 100))

def searchMatrix(matrix, target: int) -> bool:
        n = len(matrix[0]) - 1
        i = 0
        print("Hi")
        while i <= n:
            print(i)
            if target >= matrix[i][0] and target <= matrix[i][n]:
                break
            elif target > matrix[i][n]:
                i += 1
            else:
                return False
        print("Got here")
        left = 0 
        right = n
        while left <= right: 
            mid = (left + right) // 2

            if target > matrix[i][mid]:
                left = mid + 1
            elif target < matrix[i][mid]:
                right = mid -1
            else: 
                return True
        return False
    
searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)