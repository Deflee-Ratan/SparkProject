#Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[mini]:
                mini = j
        temp = arr[mini]
        arr[mini] = arr[i] 
        arr[i] = temp
    return arr

arr = list(map(int,input("\nEnter space seperated array elements: ").split()))
print("\nThe sorted array is:",selection_sort(arr))