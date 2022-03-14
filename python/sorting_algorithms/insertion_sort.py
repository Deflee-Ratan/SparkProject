#Insertion Sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key         
    return arr

arr = list(map(int,input("\nEnter space seperated array elements: ").split()))
print("\nThe sorted array is:",insertion_sort(arr))