

def merge(arr,l,m,h):
    n1=m-l+1
    n2=h-m
    L=arr[l:l+n1]
    R=arr[m+1:m+1+n2]
    
    print(L,R)
    i=0
    j=0
    k=l

    while i < n1 and j <n2:

        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    while i<n1:
        
        arr[k]=L[i]
        k+=1
        i+=1
    while j<n2:
        
        arr[k]=R[j]
        j+=1
        k+=1
    

def mergeSort(arr,l,h):
    if l<h:

        m = l+(h-l)//2

        mergeSort(arr,l,m)
        mergeSort(arr,m+1,h)
        merge(arr,l,m,h)



arr = [3, 1, 5, 2, 7, 0]
mergeSort(arr,0,len(arr)-1)
print(arr)
