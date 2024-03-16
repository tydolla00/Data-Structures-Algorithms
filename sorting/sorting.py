# Bubble Sort, Merge Sort, Bucket Sort, Selection 
class Sorting():
    def __init__(self, arr) -> None:
        self.arr = arr
    def merge_sort(self, start, end):
        def merge(s, m, e):
            # Copy the sorted left & right halfs to temp arrays
            L = self.arr[s: m + 1]
            R = self.arr[m + 1: e + 1]

            i = 0 # index for L
            j = 0 # index for R
            k = s # index for arr

            # Merge the two sorted halfs into the original array
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    self.arr[k] = L[i]
                    i += 1
                else:
                    self.arr[k] = R[j]
                    j += 1
                k += 1

            # One of the halfs will have elements remaining
            while i < len(L):
                self.arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                self.arr[k] = R[j]
                j += 1
                k += 1
                
        if end - start + 1 <= 1:
            return 
        
        m = (start + end) // 2
        self.merge_sort(start, m)
        self.merge_sort(m + 1, end)
        merge(start,m,end)
        
    def bucket_sort(self):
        pass
    def selection_sort(self):
        for i in range(0, len(self.arr)):
            j = i+1
            while j < len(self.arr):
                if self.arr[i] > self.arr[j]:
                    self.swap(i, j)
                j+=1
                
    def bubble_sort(self):
        left,right= 0,len(self.arr) - 1
        while left < right:
            while left + 1 < len(self.arr) and left < right:
                if self.arr[left] > self.arr[left+1]:
                    self.swap(left, left+1)
                left+=1
            left = 0
            right -= 1
                
    def quick_Sort(self, start, right): # Needs to be fixed.
        if right - start - 1 <= 1:
            return self.arr
        
        pivot = self.arr[start + right // 2]
        left = start
        
        for i in range(left,right):
            if self.arr[i] < pivot:
                self.swap(left, i)
                left += 1
                
        self.quick_Sort(start, pivot)
        self.quick_Sort(pivot+1, right)
        
    def insertion_sort(self):
        for i in range(1,len(self.arr)):
            j = i -1
            while j >= 0 and self.arr[j+1] < self.arr[j]:
                self.swap(j, j+1)
                j-=1
                
    def print_array(self):
        print(self.arr)
        
    def swap(self,val1, val2):
        temp = self.arr[val1]
        self.arr[val1] = self.arr[val2]
        self.arr[val2] = temp
        
sort = Sorting([100,10, 8, 5, 2, 3, 4])
# sort = Sorting([38,27,43,10])
sort.quick_Sort(0, len(sort.arr)-1)
sort.print_array()