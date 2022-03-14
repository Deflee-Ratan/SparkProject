#Merge Sort
def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        a = merge_sort(arr[:mid])
        b = merge_sort(arr[mid:])
        return merge(a,b)
    return arr

def merge(a,b):
    i=j=k=0
    tmp =[0]*(len(a)+len(b))
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            tmp[k] = a[i]
            i+=1
            k+=1
        else:
            tmp[k] = b[j]
            j+=1
            k+=1
    while i<len(a):
        tmp[k]=a[i]
        k+=1
        i+=1
    while j<len(b):
        tmp[k]=b[j]
        k+=1
        j+=1
    return tmp

    
arr = list(map(int,input("\nEnter space seperated array elements: ").split()))
print("\nThe sorted array is:",merge_sort(arr))