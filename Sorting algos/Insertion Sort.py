#Insertion Sort

arr = [5,2,7,1,4]
n = len(arr)
j = 0
temp = 0
for i in range(1,n):
    temp = arr[i]
    j = i-1

    while(j>=0 and arr[j]>temp):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp
print(arr)
