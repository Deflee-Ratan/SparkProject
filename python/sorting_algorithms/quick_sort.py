#Quick Sort
def quick_sort(arr):
    if len(arr)>1:
        j = partition(arr)
        arr[0:j] = quick_sort(arr[0:j])
        arr[j+1:len(arr)] = quick_sort(arr[j+1:len(arr)])
    return arr

def partition(arr):
    
    pivot = arr[0]
    i=1
    j=len(arr)-1
    while i<j:
        while i<len(arr) and arr[i]<pivot:
            i+=1
        while j>=0 and arr[j]>pivot:
            j-=1
        if i<j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    tmp = arr[0]
    arr[0] = arr[j]
    arr[j] = tmp
    return j


arr = list(map(int,input("\nEnter space seperated array elements: ").split()))
print("\nThe sorted array is:",quick_sort(arr))