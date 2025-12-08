

def heapSort(arr) :
    n = len(arr)
    
    def heapify (i,size) :
        largest = i
        left = 2*i + 1
        right = 2*i + 2
        
        if left < size and arr[left] > arr[largest]:
            largest = left
        
        if right < size and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(largest, size)
    
    # building the max heap
    for i in range (n//2-1,-1,-1) :
        heapify(i,n)
    
    " sorting"
    size = n 
    for i in range(n-1,0,-1) :
        arr[i] , arr[0] = arr[0] ,arr[i]
        size -= 1
        heapify(0,size)
    return arr

nums=[3,2,4,5,1]
print(heapSort(nums))