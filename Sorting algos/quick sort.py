

def partition(arr,l,h):
    pivot = arr[l]
    i=l+1
    j=h
    while(i<=j):

        while i <= j and arr[i]<=pivot:
            i+=1
        while i <= j and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[l],arr[j]=arr[j],arr[l]
    return j
    
        


def qs(arr,l,h):
    if l<h:
        pi = partition(arr,l,h)
        qs(arr,l,pi-1)
        qs(arr,pi+1,h)

nums = [10, 7, 8, 9, 1, 5]
n=len(nums)
qs(nums,0,n-1)
print(nums)
        


