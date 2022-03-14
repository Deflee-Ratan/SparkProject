#Radix Sort
def radix_sort(arr):
    for k in range(1,len(str(max(arr)))+1):
        buckets = [[]]*10
        for i in arr:
            c=(i%(10**k))//(10**(k-1))
            if len(buckets[c])==0:
                buckets[c]=[i]
            else:
                buckets[c].append(i)
            tmp = []
        for i in range(10):
            tmp.extend(buckets[i])
        
        arr = tmp

    return arr

arr = list(map(int,input("\nEnter space seperated array elements: ").split()))
print("\nThe sorted array is:",radix_sort(arr))